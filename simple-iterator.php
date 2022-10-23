<?php

/*
Copyright (c) 2022 Dirk Engel, https://skriptschmiede.de

NAME
    simple-iterator.php - Demo script to explain the
    iterator pattern in PHP
SYNOPSIS
    php simple-iterator.php
DESCRIPTION
    Simple iterator class example:
    (1) __construct method is the iterator's constructor.
    (2) rewind method: go back to the iterator's initial state.
    (3) current method: return current iteration value.
    (4) key method: return current key.
    (5) next method: increment position.
    (6) valid method: check validity of current position.
LICENSE
    This file is licensed under the MIT License.
    License text available at https://opensource.org/licenses/MIT
 */

class TypingIterator implements Iterator
{
    private $position;
    private $my_container;

    public function __construct(array $my_container = [])
    {
        $this->position = 0;
        $this->my_container = $my_container;
    }

    public function rewind(): void
    {
        $this->position = 0;
    }

    public function current(): mixed
    {
        $item = $this->my_container[$this->position];
        return [gettype($item), $item];
    }

    public function key(): int
    {
        return $this->position;
    }

    public function next(): void
    {
        ++$this->position;
    }

    public function valid(): bool
    {
        return isset($this->my_container[$this->position]);
    }
}

$cont_to_be_iterated = new TypingIterator([[true, 7.7], 9, 'X']);

echo "\nOur 'typing' generator/iterator:\n";
foreach ($cont_to_be_iterated as $element) {
    echo $element[0], "\t\t", json_encode($element[1]), "\n";
}
