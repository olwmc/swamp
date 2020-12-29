( Testing simple variable. Should print 576 )
variable beans
123 beans !
beans @ . cr


( Testing additional variable to see if 
  it can do memory correctly. Should print 777 )
variable court
777 court !
court @ . cr


( Function test. Should print 45 [0+1+2+3+4+5+6+7+8+9+10] )
: foo 0 10 0 do i + loop ;
foo . cr


( Loop test. Should print "Wee woo" twice )
2 0 do
      ." Wee woo" cr
    loop


( Conditional test. Should print "Hello!" and then not print )
-1 
if ." Hello!" cr then

0
if ." I will never be seen!" cr then

( Testing constants. Should print 34 )
34 constant test_const
test_const . cr
