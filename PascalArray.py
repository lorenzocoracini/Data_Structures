class PascalArray:
    def __init__(self, first_position, last_position):
        self._first_position = first_position
        self._last_position = last_position
        self._length = (self._first_position - self._last_position) + 1
        self._array = self._length * []

    def set(self, value, position):
        try:
            self._array[position - self._first_position] = value
        except ValueError:
            return ("Array without this position!")

    def get(self, position):
        if (position - self._first_position < 0):
            return ("Array without this position!")
        return self._array[position - self._first_position]
