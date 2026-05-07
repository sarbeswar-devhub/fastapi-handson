from app.db.models.user import User


def fetch_users(db, user):
    users = db.query(
        User.id,
        User.name,
        User.email,
        User.phone,
        User.address,
        User.is_active,
        User.created_at
    ).filter(
        User.is_active == True
    ).all()

    print(users)

    return {"result": users}

def fetch_user_by_id(db, user_id):
    user = db.query(
        User.id,
        User.name,
        User.email,
        User.phone,
        User.address,
        User.created_at
    ).filter(
        User.is_active == True,
        User.id == user_id
    ).all()

    return {"result": user}