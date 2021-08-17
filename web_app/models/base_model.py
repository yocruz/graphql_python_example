from web_app import DB as db


class BaseModel(object):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def reload(self):
        return db.session.refresh(self)


class SerializableModel:

    def __init__(self):
        self.SERIALIZABLE_FIELDS = []

    def to_json(self):
        serialized_data = {}
        for f in self.SERIALIZABLE_FIELDS:
            if hasattr(self, f):
                val = getattr(self, f)
                serialized_data[f] = val
            else:
                raise Exception(
                    f'Field {f} does not exists in class {self.__class__}')
        return serialized_data

    @classmethod
    def from_json(cls, object_data, strict=False):
        """
        Creates a new object from a dict containing the model 
        values.
        If strict is set to true, any field not present in the original
        model will raise an exception
        """
        new_object = cls()
        for key, val in object_data.items():
            if hasattr(new_object, key):
                setattr(new_object, key, val)
            elif strict:
                raise Exception(
                    f'Additional attributes not allow. Attributte {key} does not exists in {cls}')
        return new_object
