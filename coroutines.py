#
# Copyright (c) 2022 Dirk Engel, https://skriptschmiede.de
#
# NAME
#     coroutine.py - Demo script to explain synchronous
#     coroutines in Python
#
# SYNOPSIS
#     python coroutine.py
# DESCRIPTION
#     Three synchronous coroutines are defined and run.
#     One data producer, one filter, and one data consumer.
# LICENSE
#     This file is licensed under the MIT License.
#     License text available at https://opensource.org/licenses/MIT
#


def producer(x):
    """Data producer that creates numbers from 1 to 7"""

    print("Producer: I started my coroutine")
    print(x.send(None))
    num = 1
    while num <= 7:
        print(f"Producer: I created {num}")
        r = x.send(num)
        print(f"Producer: My consumer returned {r}")
        num = num + 1


def filter(x):
    """Data filter that passes all even numbers"""

    y = "Filter: I started my coroutine"
    print(x.send(None))
    while True:
        num = yield y
        print(f"Filter: Received {num}")

        if num % 2 == 0:
            r = x.send(num)
            print(f"Filter: Transmitted {num}")
            print(f"Filter: My consumer returned {r}")
            y = "'passed'"
        else:
            print(f"Filter: Blocked {num}")
            y = "'blocked'"


def consumer():

    """Data consumer that eats the received numbers"""

    y = "Consumer: I started my coroutine"
    while True:
        num = yield y
        print(f"Consumer: Eating {num}")
        y = "'eaten'"


if __name__ == "__main__":
    producer(filter(consumer()))
