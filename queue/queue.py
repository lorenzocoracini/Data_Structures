class Queue:
    def _init_(self, max):
        self._queue = []
        self._lenght = len(self._queue)
        self._max = max
        self._start = self._queue[0]
        self._final = self.set_final_queue()

    def set_final_queue(self):
        if self._lenght > 0:
            return self._queue[self._lenght - 1]

    def verify_queue_is_not_empty(self) -> bool:
        return self._lenght == 0

    def verify_queue_is_not_full(self) -> bool:
        return self._lenght == self._max

    def add_in_queue(self, element):
        if self.verify_queue_is_not_full():
            self._queue[self._final] = element

    def take_out_of_queue(self):
        if self.verify_queue_is_not_empty():
            self._queue.remove(self._start)
