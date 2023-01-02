import pytest
from mongoengine import connect


@pytest.fixture()
def mock_get_db_connection(mocker):
    return mocker.patch(
        'application.budget.db.get_db_connection',
        return_value=connect(
            'mongoenginetest',
            host='mongomock://localhost'
        )
    )
