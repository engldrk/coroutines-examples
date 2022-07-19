import sys


class TypingIterator:
    def __init__(self, my_container):
        """
        Example works for sequencial container objects
        with length and index from zero on defined.
        """
        try:
            # we don't do class based checks here,
            # we prefer duck typing...
            len(my_container)  # check length function.
            my_container[0]  # check element zero.
            my_container[-1]  # check last element.
        except:
            print(
                (
                    f"Error: No length/index defined: "
                    f"{type(my_container).__name__} "
                    f"{str(my_container)}!\n"
                )
            )
            sys.exit(1)
        else:
            self.index = 0  # always start at 0.
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


# for-in loop over our TypedIterator.
print("\nOur custom typed iterator:")
for element in TypingIterator([{2, 8}, 9, "8"]):
    print(repr(element))

# for-in loop over plain vanilla standard iterator.
print("\nStandard iterator:")
for element in [{2, 8}, 9, "8"]:
    print(repr(element))
