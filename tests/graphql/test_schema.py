import pytest
from graphql.execution import ExecutionResult

from tests import app_client

from flask.testing import FlaskClient
from web_app import DB as db
from web_app.repositories.user_repo import UserRepo


class TestSchema():

    def test_schema_query(self, app_client: FlaskClient):
        with app_client.application.app_context():
            repo = UserRepo()
            user_data = {
                'username': 'test_user',
                'email': 'a@a.com',
                'gender': 'M'
            }
            new_user = repo.create(user_data)
            assert new_user.id == 1

            from web_app.graphql.schema import schema

            query = '''
                query {
                  users {
                    username,
                    email
                  }
                }
            '''
            result: ExecutionResult = schema.execute(query, context_value={'session': db})

            assert result.data == {'users': [{'username': 'test_user', 'email': 'a@a.com',}]}