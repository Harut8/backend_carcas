from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.helpers.db import DbHelper
from app.helpers.jwt import create_access_token, create_refresh_token
from app.helpers.middlewares import get_current_user, username_password_validation
from app.routers.auth.crud import create_user
from app.routers.auth.schemas import TokenInfo, UserCreateSchema, UserSchema

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.get("/health-check")
async def health_check():
    return {"message": "App is up and running!"}


@auth_router.post("/sign-in", response_model=TokenInfo)
async def signin(credentials: UserSchema = Depends(username_password_validation)):
    token_payload = credentials.model_dump(exclude={"password"})
    return {
        "access_token": create_access_token(token_payload),
        "refresh_token": create_refresh_token(token_payload),
        "token_type": "Bearer",
    }


@auth_router.post("/sign-up")
async def signup(user: UserCreateSchema, session: AsyncSession = Depends(DbHelper.get_session)):
    await create_user(session, user)
    return {"message": "User created"}


@auth_router.get("/me", response_model=UserSchema)
async def me(user: UserSchema = Depends(get_current_user)):
    return user
