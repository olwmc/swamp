variable i
0 i !

: add-one-to-i
    ( Increment i )
    i @ 1 +

    ( Set i )
    i !
;

begin
    add-one-to-i
    
    ( Get i )
    i @ 10 =

    i @ . cr
until