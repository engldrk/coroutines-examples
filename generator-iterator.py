#
# Copyright (c) 2022 Dirk Engel, https://skriptschmiede.de
#
# NAME
#     generator-iterator.py - Demo script to explain the
#     generator/iterator pattern in Python
# SYNOPSIS
#     python iterator-generator.py
# DESCRIPTION
#     Iterator from generator function example:
#     (1) generator function has 'yield' instead of 'return'.
#     (2) __next__ method is defined automatically.
#     (3) __iter__ method is defined automatically.
#     (4) StopIteration is raised automatically.
# LICENSE
#     This file is licensed under the MIT License.
#     License text available at https://opensource.org/licenses/MIT
#


def typing_iterator_generator(my_container):
    """
    Example works for sequencial container objects.
    Pre-condition: For-in loop must be runable on
    my_container.
    """

    for item in my_container:
        yield ((type(item).__name__), item)


if __name__ == "__main__":

    container_to_be_iterated = [{2, 8}, 9, "8"]

    # for-in loop over our generator typing_iterator.
    print("\nOur 'typing' generator/iterator:")
    for element in typing_iterator_generator(container_to_be_iterated):
        print(repr(element))
