#
# iterator/generator as coroutine example:
#
# (1) generator function is defined by
#     'yield' instead of 'return'.
# (2) __next__ method is defined automatically.
# (3) __iter__ method is defined automatically.
# (4) StopIteration is raised automatically.
#


def typing_iterator_coroutine(my_container):
    """
    Example works for sequencial container objects.

    Pre-condition: For-in loop must be runable on
    my_container.

    Exception handling is skipped for brevity!
    """

    for item in my_container:
        prefix = yield
        yield (str(prefix) + str(type(item).__name__), item)


if __name__ == "__main__":

    container_to_be_iterated = [{2, 8}, 9, "8"]

    # calling the same iterator object manually via 'next'/'send'
    print("\nOur custom typed iterator/coroutine via 'next'/'send':")
    coroutine_object = typing_iterator_coroutine(container_to_be_iterated)
    count = 0
    while True:
        try:
            count += 1
            prefix = str(count)
            next(coroutine_object)
            print(coroutine_object.send(str(prefix) + " => "))  # type: ignore
        except StopIteration:
            print("Last iteration!")
            coroutine_object.close()
            break
