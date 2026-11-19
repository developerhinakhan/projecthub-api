import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.database import Base, get_db
from app.main import app
from app.models.project import Project  # noqa: F401
from app.models.project_member import ProjectMember  # noqa: F401
from app.models.team import Team  # noqa: F401
from app.models.team_member import TeamMember  # noqa: F401
from app.models.user import User  # noqa: F401

TEST_DATABASE_URL = make_url(settings.database_url).set(database="projecthub_test")

if not TEST_DATABASE_URL.database.endswith("_test"):
    raise RuntimeError("Refusing to run tests on a non-test database")

test_engine = create_engine(TEST_DATABASE_URL)


TestSession = sessionmaker(autoflush=False, bind=test_engine)


@pytest.fixture
def db_session():
    Base.metadata.create_all(test_engine)
    db = TestSession()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(test_engine)


@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()
