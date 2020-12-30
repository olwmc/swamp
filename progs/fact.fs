( Factorial function )
: fact
    ( Add one to input )
    1 +
    
    ( Push 1 and swap with input to act
      as loop upper bound)
    1 swap 1

    ( Do loop multiplying by i from 1 to n)
    do
        i *
    loop
;