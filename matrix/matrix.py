class Matrix:
    def __init__(self, num_rows, num_cols):
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._array_of_matrix = (self._num_rows * self._num_cols) * []

    def set(self, row, col, value):
        _index = ((row - 1) * self._num_cols) + (col - 1)
        self._array_of_matrix[_index] = value

    def get(self, row, col):
        _index = ((row - 1) * self._num_cols) + (col - 1)
        return self._array_of_matrix[_index]
