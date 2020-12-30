( Recursively counts down from n)
: foo
    ( Check if != )
    dup 0 = invert
    if
        dup 1 - foo
    then
;

( Push 20 to the stack, call foo, list stack)
20 foo ?