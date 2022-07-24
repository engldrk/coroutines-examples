#
# iterator from generator function example:
#
# (1) generator function is defined by
#     'yield' instead of 'return'.
# (2) __next__ method is defined automatically.
# (3) __iter__ method is defined automatically.
# (4) StopIteration is raised automatically.
#


def typing_iterator_generator(my_container):
    """
    Example works for sequencial container objects.

    Pre-condition: For-in loop must be runable on
    my_container.

    Exception handling is skipped for brevity!
    """

    for item in my_container:
        yield (type(item).__name__, item)


if __name__ == "__main__":

    container_to_be_iterated = [{2, 8}, 9, "8"]

    # for-in loop over our generator typing_iterator.
    print("\nOur custom typed iterator/generator:")
    for element in typing_iterator_generator(container_to_be_iterated):
        print(repr(element))

    # calling the same iterator object manually via 'next'
    print("\nOur custom typed iterator/generator via 'next':")
    iterator_object = typing_iterator_generator(container_to_be_iterated)
    while True:
        try:
            print(next(iterator_object))
        except StopIteration:
            print("Last iteration!")
            break
