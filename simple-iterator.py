#
# Copyright (c) 2022 Dirk Engel, https://skriptschmiede.de
#
# NAME
#     simple-iterator.py - Demo script to explain the
#     iterator pattern in Python
# SYNOPSIS
#     python simple-iterator.py
# DESCRIPTION
#     Simple iterator class example:
#     (1) __init__ method sets start values.
#     (2) __next__ method is customized to run our iteration.
#     (3) __iter__ method returns same object.
#     (4) End of iteration raises StopIteration.
# LICENSE
#     This file is licensed under the MIT License.
#     License text available at https://opensource.org/licenses/MIT
#


class TypingIterator:
    def __init__(self, my_container):
        """
        Example works for sequencial container objects.
        Pre-condition: Length and index of my_container
        must be defined from [0] to [-1].
        """

        self.index = 0
        self.my_container = my_container

    def __iter__(self):
        """
        We already have the __next__ method,
        so we return 'self' (same object) here.
        """
        return self

    def __next__(self):
        """
        Method __next__ contains the whole iterator logic.
        You could do any resumable calculation here.
        """
        # protocol requires: last element => StopIteration.
        if self.index + 1 > len(self.my_container):
            raise StopIteration
        # customized iteration values: types added
        value = (
            type(self.my_container[self.index]).__name__,
            self.my_container[self.index],
        )
        self.index += 1

        return value


if __name__ == "__main__":

    container_to_be_iterated = [{2, 8}, 9, "8"]

    # for-in loop over our simple iterator TypedIterator.
    print("\nOur 'typing' iterator:")
    for element in TypingIterator(container_to_be_iterated):
        print(repr(element))
