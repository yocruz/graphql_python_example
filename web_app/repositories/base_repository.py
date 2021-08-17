from web_app import DB as db


def RequiredAttributes(*required_attrs):
    class RequiredAttributteMeta(type):
        def __init__(cls, name, bases, obj_dict):
            missing_attrs = []
            for attr in required_attrs:
                if not hasattr(cls, attr):
                    missing_attrs.append(attr)
            if missing_attrs:
                raise AttributeError(
                    f'Attributes missing in class declaration {missing_attrs} ')
    return RequiredAttributteMeta


class BaseRepository(metaclass=RequiredAttributes('model')):

    model = None  # all the subclasses have to define the model they implement

    def create(self, data_dict):
        new_object = self.model.from_json(data_dict)
        db.session.add(new_object)
        db.session.commit()
        new_object.reload()
        return new_object

    def remove(self, object_id):
        pass

    def update(self, object_id, new_data):
        pass
