class Stack:
    def __init__(self, max_top):
        self._max_top = max_top
        self._top = -1
        self._stack = []

    def push(self, value):
        _validate = self._valid_if_is_full()
        if _validate:
            self._stack.append(value)
            self._top += 1

    def pop(self):
        _validate = self._valid_if_is_empty()
        if _validate:
            self._stack.pop(self._top)
            self._top -= 1

    def _valid_if_is_full(self):
        if self._top == self._max_top:
            print("Stack full!")
        else:
            return True

    def _valid_if_is_empty(self):
        if self.lenght() == 0:
            print("Stack empty")
        else:
            return True

    def lenght(self):
        return self._top + 1
