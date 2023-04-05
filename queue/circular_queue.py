class CircularQueue:
    def _init_(self, max):
        self._max = max
        self._queue = [] * max
        self._start = 0
        self._final = 0
        self._number_elements = 0
        self._lenght = len(self._queue)

    def verify_queue_is_not_empty(self) -> bool:
        return self._lenght == 0

    def verify_queue_is_not_full(self) -> bool:
        return self._lenght == self._max

    def add_in_queue(self, element):
        if self.verify_queue_is_not_full():
            self._queue[self._final] = element
            self._number_elements += 1
            self._final += 1

        if self._final == self._max:
            self._final = 0

    def take_out_of_queue(self):
        if self.verify_queue_is_not_empty():
            self._start += 1
            self._number_elements -= 1
            if self._start == self._max:
                self._start = 0