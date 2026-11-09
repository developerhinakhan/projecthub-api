from sqlalchemy import create_engine
from sqlalchemy.engine import make_url

from app.config import settings

TEST_DATABASE_URL = make_url(settings.database_url).set(database="projecthub_test")

if not TEST_DATABASE_URL.database.endswith("_test"):
    raise RuntimeError("Refusing to run tests on a non-test database")

test_engine = create_engine(TEST_DATABASE_URL)
