#
# simple iterator class example:
#
# (1) __init__ method sets start values.
# (2) __next__ method is customized to run our
#     "special" typed iteration.
# (3) __iter__ method returns same object, because it
#     already is iterable via __next__. Method __iter__ will
#     be called by for-in loop automatically. Otherwise
#     object would not be iterable and we get an error.
# (4) End of iteration raises StopIteration.
#


class TypingIterator:
    def __init__(self, my_container):
        """
        Example works for sequencial container objects.

        Pre-condition: Length and index of my_container
        must be defined from [0] to [-1].

        Exception handling is skipped for brevity!
        """

        self.index = 0
        self.my_container = my_container

    def __iter__(self):
        """
        we already have the __next__ method,
        so we return 'self' (same object) here.
        """
        return self

    def __next__(self):
        """
        __next__ method contains the whole iterator logic.
        you could do any resumable calculation here.
        """
        # protocol requires: last element => StopIteration.
        if self.index + 1 > len(self.my_container):
            raise StopIteration
        # here are the customized iteration values!
        value = (
            type(self.my_container[self.index]).__name__,
            self.my_container[self.index],
        )
        self.index += 1

        return value


if __name__ == "__main__":

    container_to_be_iterated = [{2, 8}, 9, "8"]

    # for-in loop over our simple iterator TypedIterator.
    print("\nOur custom typed iterator:")
    for element in TypingIterator(container_to_be_iterated):
        print(repr(element))

    # for-in loop over plain vanilla standard iterator.
    print("\nStandard iterator:")
    for element in container_to_be_iterated:
        print(repr(element))
