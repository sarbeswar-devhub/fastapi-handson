from fastapi import APIRouter
from app.modules.auth.router import router as auth_router
from app.modules.user.router import router as user_router

# config version 1.0 api routes
api_router_v1 = APIRouter(prefix="/api/v1")

# includes to verison 1.0 routes
api_router_v1.include_router(auth_router)
api_router_v1.include_router(user_router)