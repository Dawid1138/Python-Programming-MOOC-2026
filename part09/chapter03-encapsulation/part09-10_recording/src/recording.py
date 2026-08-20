class Recording:
    def __init__(self, length):
        if length < 0:
            raise ValueError("The amount must not be below zero")
        self._length = length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_length):
        if new_length < 0:
            raise ValueError("The amount must not be below zero")
        self._length = new_length