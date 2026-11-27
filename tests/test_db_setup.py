from sqlalchemy import inspect


def test_tables_exist(db_session):
    names = inspect(db_session.get_bind()).get_table_names()
    assert "users" in names
