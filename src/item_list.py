# Libraries



class ItemList:

    def __init__(self):
        # initialise instance attributes
        self._list = list()
        pass

    def __del__(self):
        # initialise instance attributes
        pass

    # @staticmethod

    def add_item(self, item):
        """ Adds an item to the list

        :param item:
        """
        self._list.append(item)

    def get_item_from_title(self, identifier):
        """ Checks if an item is in the list based on its Title

        :param identifier: Title
        :return: item
        """
        for item in self._list:
            item_identifier = item.get_title()
            if identifier == item_identifier:
                return item

    def get_item_from_id(self, identifier):
        """ Checks if an item is in the list based on its ID

        :param identifier: ID
        :return: item
        """
        for item in self._list:
            item_identifier = item.get_id()
            if identifier == item_identifier:
                return item

    def number_of_items(self):
        """ Gets the number of items in the list

        :return: Number of items in the list
        """
        return len(self._list)

    def get_fines(self, item):
        """ Calculates the fine of an item

        :param item:
        :return: Fine for the item
        """
        return item.calc_finedue()

    def get_total_fines(self):
        """ Calculates the total amount of fines of overdue items

        Return: Fine for all
        :return:
        """
        fines = 0
        for item in self._list:
            fines += item.calc_finedue()
        return fines

    def checkout_item(self, item, date=None):
        """ Adds an item to the list and set the checkout date

        :return:
        """
        self._list.append(item)
        item.set_checkoutdate(past_date=date)

    def return_item(self, item):
        """ Removes an item to the list and reset the checkout date

        :return:
        """
        self._list.remove(item)
        item.reset_checkoutdate()

if __name__ == '__main__':
    pass