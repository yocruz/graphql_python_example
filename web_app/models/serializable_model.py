
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
