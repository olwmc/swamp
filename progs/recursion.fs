( Recursively counts down from n)
: foo
    ( Check if != )
    dup 0 = invert
    if
        dup 1 - foo
    then
;