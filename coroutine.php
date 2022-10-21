<?php

/*
Copyright (c) 2022 Dirk Engel, https://skriptschmiede.de

NAME
    coroutine.php - Demo script to explain synchronous
    coroutines in PHP
SYNOPSIS
    php coroutine.py
DESCRIPTION
    Three generators are calling one another:
    One data producer, one filter, and one data consumer.
LICENSE
    This file is licensed under the MIT License.
    License text available at https://opensource.org/licenses/MIT
*/

function producer($x)
{
    echo "Producer: I started my coroutine\n";
    $num = 1;
    while ($num <= 4) {
        echo "Producer: Created $num\n";
        $r = $x->send($num);
        echo "Producer: My consumer returned: $r\n";
        $num = $num + 1;
    }
}

function filter($x)
{
    echo "Filter: I started my coroutine\n";
    $y = '';
    while (true) {
        $num = yield $y;
        echo "Filter: Received $num\n";
        if ($num % 2 == 0) {
            $r = $x->send($num);
            echo "Filter: Transmitted $num\n";
            echo "Filter: My consumer returned: $r\n";
            $y = "I will pass $num";
        } else {
            echo "Filter: Blocked $num\n";
            $y = "I will block $num";
        };
    }
}

function consumer()
{
    echo "Consumer: I started my coroutine\n";
    $y = '';
    while (true) {
        $num = yield $y;
        echo "Consumer: Eating $num :-)\n";
        $y = "I will eat $num";
    }
}


function main()
{
    producer(filter(consumer()));
};

main();
