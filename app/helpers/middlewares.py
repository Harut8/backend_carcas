from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.helpers.db import DbHelper
from app.helpers.exceptions import AuthenticationFailedError, PermissionDeniedError
from app.helpers.jwt import jwt_decode, validate_password
from app.routers.auth.crud import get_user_by_email
from app.routers.auth.models import User
from app.routers.auth.schemas import UserPasswordSchema, UserSchema

security_bearer = HTTPBearer()


async def username_password_validation(
    session: AsyncSession = Depends(DbHelper.get_session),
    credentials: UserPasswordSchema = Depends(),
) -> UserSchema:
    user: User = await get_user_by_email(session, credentials.email)
    user_schema: UserSchema = UserSchema.model_validate(user)
    if user and validate_password(credentials.password, user.password.encode()):
        return user_schema
    raise AuthenticationFailedError()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security_bearer),
    session: AsyncSession = Depends(DbHelper.get_session),
) -> UserSchema:
    user_email = jwt_decode(credentials.credentials).get("email")
    if not user_email:
        raise PermissionDeniedError
    user: User = await get_user_by_email(session, user_email)
    return UserSchema.model_validate(user)
