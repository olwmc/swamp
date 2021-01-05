: fizz?  3 mod 0 = dup if ." Fizz" then ;
: buzz?  5 mod 0 = dup if ." Buzz" then ;
: fizz-buzz?  dup fizz? swap buzz? or invert ;
: do-fizz-buzz  1 do i fizz-buzz? if i . then cr loop ;

( Fizz Buzz )
45 do-fizz-buzz