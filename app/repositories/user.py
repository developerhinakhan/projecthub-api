from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class AuthRepo:
    def get_user_by_email(self, db: Session, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        return db.scalar(stmt)

    def add(self, db: Session, user: User) -> User:
        db.add(user)
        return user


auth_repo = AuthRepo()
