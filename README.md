# Swamp
A FORTH-like language.

## Example:
```forth
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
```
Output:
```python
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
- [X] begin-until loop
- [X] RNG
- [X] Turn input into an op instead of word subclass
- [X] Stack snapshot log `save`
- [X] Unimplemented operations
- [ ] Refactor program structure for clarity
- [ ] Correct and descriptive error messages
- [ ] Debug mode / dump option
- [ ] Error checking
- [ ] Language guide

### Resources/References
The *wonderful* [EasyForth](https://skilldrick.github.io/easyforth/) by Skilldrick

[Starting Forth](https://www.forth.com/starting-forth/)

<!-- ## Other goals:
- [ ] Virtual machine
- [ ] VM compiler -->
