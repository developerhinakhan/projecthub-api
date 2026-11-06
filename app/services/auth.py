from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user import auth_repo
from app.schemas.user import UserCreate


class EmailAlreadyRegisteredError(Exception):
    pass


def register_user(db: Session, data: UserCreate) -> User:
    email = data.email.lower()
    existing = auth_repo.get_user_by_email(db, email)
    if existing:
        raise EmailAlreadyRegisteredError
    hashed = hash_password(data.password)
    user = User(email=email, hashed_password=hashed, full_name=data.full_name)
    auth_repo.add(db, user)
    db.commit()
    db.refresh(user)
    return user
