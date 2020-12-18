from sys import maxsize


class Group:

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.name is None or other.name is None or self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
