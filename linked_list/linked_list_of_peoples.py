from linked_list.people import People


class LinkedList:
    def _init_(self, max_len):
        self.__max_len = max_len
        self.__first = 0
        self.__last = 0
        self.__number_of_items = 0

    def insert(self, people: People):
        if not self.is_full():
            if self.is_empty():
                self.__first = people
                self.__last = people

            else:
                self.__last.next = people
                self.__last = people
            self.__number_of_items += 1

    def take_out(self):
        if not self.is_empty():
            self.__first = self.__first.next
            self.__number_of_items -= 1

    def first_item(self):
        return self.__first

    def last_item(self):
        return self.__last

    def is_empty(self):
        return self.__number_of_items == 0

    def length(self):
        return self.__number_of_items

    def is_full(self):
        return self.__number_of_items == self.__max_len
