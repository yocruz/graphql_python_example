from sqlalchemy.exc import NoResultFound
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

    def get(self, id):
        return self.model.get(id)

    def create(self, data_dict):
        new_object = self.model.from_json(data_dict)
        db.session.add(new_object)
        db.session.commit()
        new_object.reload()
        return new_object

    def delete(self, object_id):
        obj = self.model.query.get(object_id)
        if obj is not None:
            db.session.delete(obj)
            db.session.commit()
            return obj
        return None

    def update(self, object_id, **kwargs):
        obj = self.model.query.get(object_id)
        if obj is None:
            raise NoResultFound(f'The {self.model.__class__.__name__} with id {object_id} does not exists')

        for key, value in kwargs.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        db.session.commit()
        obj.reload()
        return obj
