from fibonacci import *
from scrabble import *
from list_duplicates import *

# run fibonacci
print(fib())

# run scrabble
print(scrabble_calc())

# run list_duplicates
test = [1, 1, 1, 1, 2, 3, 3, 1, 1]
str_test = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'e']

print(no_dup(test))
print(no_dup(str_test))