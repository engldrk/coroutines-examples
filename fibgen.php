<?php
$gener = (function () use (&$gener): Generator {
    $userfunc = function () use (&$gener): Generator {
        register_shutdown_function(function () use (&$gener) {
            $gener->send('test');
        });
        return yield 'test';
    };
    $parm = yield from $userfunc();
    echo "Value used to resume fiber: ", $parm, PHP_EOL;
})();

$res = $gener->current();
echo "Value from fiber suspending: ", $res, PHP_EOL;

$fiber = new Fiber(function () use (&$fiber): void {
    $userfunc = function () use (&$fiber): string {
        register_shutdown_function(function () use (&$fiber) {
            $fiber->resume('test');
        });
        return Fiber::suspend('fiber');
    };
    $parm = $userfunc();
    echo "Value used to resume fiber: ", $parm, PHP_EOL;
});

$res = $fiber->start();
echo "Value from fiber suspending: ", $res, PHP_EOL;
