from app.db.models.user import User
from fastapi import status, HTTPException
from app.core import utils, oauth2

def login_user(db, payload):
    user = db.query(User).filter(User.email == payload.username).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    
    if not utils.verify_hashed_password(payload.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials!")

    # generate access token
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}

def register_user(db, payload):
    # check existing
    user = get_user_by_email(db, payload.email)

    if user is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exist!")
    
    # make hashed password
    hashed_password = utils.get_hashed_password(payload.password)


    new_user = User(
        name = payload.name,
        email = payload.email,
        phone = payload.phone,
        address = payload.address,
        password = hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created", "id": new_user.id}


def get_user_by_email(db, email):
    user = db.query(
            User   
        ).filter(
            User.email == email
        ).first()
    
    return user