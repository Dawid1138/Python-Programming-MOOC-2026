class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__items = []
        self.__weight = 0

    def add_item(self, item):
        if self.__capacity >= self.__weight + item.weight():
            self.__items.append(item)
            self.__weight += item.weight()
            return True
        else:
            return False

    def __str__(self):
        if len(self.__items) != 1:
            return f"{len(self.__items)} items ({self.__weight} kg)"
        else:
            return f"1 item ({self.__weight} kg)"

    def weight(self):
        return self.__weight

    def print_items(self):
        for item in self.__items:
            print(item)

    def heaviest_item(self):
        if len(self.__items) == 0:
            return None
        heaviest = 0
        heaviest_item = None
        for item in self.__items:
            if item.weight() > heaviest:
                heaviest = item.weight()
                heaviest_item = item
        return heaviest_item


class CargoHold:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__suitcases = []
        self.__weight = 0

    def add_suitcase(self, suitcase):
        if self.__capacity >= self.__weight + suitcase.weight():
            self.__suitcases.append(suitcase)
            self.__weight += suitcase.weight()
            return True
        else:
            return False

    def __str__(self):
        if len(self.__suitcases) != 1:
            return f"{len(self.__suitcases)} suitcases, space for {self.__capacity - self.__weight} kg"
        else:
            return f"1 suitcase, space for {self.__capacity - self.__weight} kg"

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()