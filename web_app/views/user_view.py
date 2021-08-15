from flask.views import MethodView

class User(MethodView):

    def get(self):
        return 'ok', 200

    def post(self):
        return 'ok', 201