<?php

/*
Copyright (c) 2022 Dirk Engel, https:skriptschmiede.de

NAME
    generator-iterator.php - Demo script to explain the
    generator/iterator pattern in PHP
SYNOPSIS
    php iterator-generator.php
DESCRIPTION
    The iterator is constructed implicitly by the simpler
    syntax of the generator's yield expression.
LICENSE
    This file is licensed under the MIT License.
    License text available at https:opensource.org/licenses/MIT
*/

function typing_iter_generator($my_container)
{
    foreach ($my_container as $item) {
        yield [gettype($item), $item];
    };
};

$cont_to_be_iterated = [[true, 7.7], 9, 'X'];

echo "\nOur 'typing' generator/iterator:\n";
foreach (typing_iter_generator($cont_to_be_iterated) as $element) {
    echo $element[0], "\t\t", json_encode($element[1]), "\n";
}
