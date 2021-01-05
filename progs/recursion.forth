( Recursively push values down from n)
: foo
    ( Check if != 1 )
    dup 1 = invert
    if
        dup 1 - foo
    then
;

10 foo

( Print stack)
?
