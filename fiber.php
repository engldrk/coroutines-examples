<?php

/*
Copyright (c) 2022 Dirk Engel, https://skriptschmiede.de

NAME
    fiber.php - Demo script to explain synchronous
    coroutines in PHP using fibers
SYNOPSIS
    php fiber.php
DESCRIPTION
    Two fibers are called independently from the main function.
    Each fiber is producing its own series of random numbers,
    one after the other.
LICENSE
    This file is licensed under the MIT License.
    License text available at https://opensource.org/licenses/MIT
*/

function make_seed()
{
    list($usec, $sec) = explode(' ', microtime());
    return $sec + $usec * 1000000;
}

$ping = new Fiber(function (): void {
    $seed = make_seed();
    echo "Ping: Made my seed $seed\n";
    srand($seed);
    $received = Fiber::suspend('ready');
    while (true) {
        echo "Ping: Received: '$received'\n";
        $num = rand(0, 2);
        $received = Fiber::suspend($num);
    }
});

$pong = new Fiber(function (): void {
    $seed = make_seed();
    echo "Pong: Made my seed $seed\n";
    srand($seed);
    $received = Fiber::suspend('ready');
    while (true) {
        echo "Pong: Received: '$received'\n";
        $num = rand(0, 2);
        $received = Fiber::suspend($num);
    }
});


function main()
{

    global $ping, $pong;

    echo "Main: Starting ping\n";
    $from_ping = $ping->start();
    echo "Main: From ping: '$from_ping'\n";

    echo "Main: Starting pong\n";
    $from_pong = $pong->start();
    echo "Main: From pong: '$from_pong'\n";

    $sum = 1;
    while ($sum > 0) {

        $from_ping = $ping->resume('go on');
        echo "Main: From ping: $from_ping\n";

        $from_pong = $pong->resume('go on');
        echo "Main: From pong: $from_pong\n";

        $sum = $from_ping + $from_pong;
    }
    echo "Main: Done!\n";
};

main();
