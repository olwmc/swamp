# Swamp
A FORTH-type language.

## Example:
```fsharp
( Recursively push values down from n)
: foo
    ( Check if != )
    dup 0 = invert
    if
        dup 1 - foo
    then
;

10 foo ?
```
Output:
```
[10,9,8,7,6,5,4,3,2,1]
```

### TODO:
- [X] Conditionals
    - [X] If
    - [X] Else
- [X] Imports
- [X] Memory allocation
- [X] User input
- [X] Method descriptors / Comments *(n -- n)*
- [ ] begin-until loop
- [ ] Unimplemented operations
- [ ] Debug mode
- [ ] Error checking

### Resources/References
The *wonderful* [EasyForth](https://skilldrick.github.io/easyforth/) by Skilldrick

[Starting Forth](https://www.forth.com/starting-forth/)

<!-- ## Other goals:
- [ ] Virtual machine
- [ ] VM compiler -->
