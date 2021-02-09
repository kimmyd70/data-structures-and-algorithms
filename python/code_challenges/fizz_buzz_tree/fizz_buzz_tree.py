

# 1. Write a function called `FizzBuzzTree` which takes a k-ary tree as an argument.

# 2. Without utilizing any of the built-in methods available to your language, determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

#     - If the value is divisible by 3, replace the value with “Fizz”

#     - If the value is divisible by 5, replace the value with “Buzz”

#     - If the value is divisible by 3 and 5, replace the value with “FizzBuzz”

#     - If the value is not divisible by 3 or 5, simply turn the number into a String (ie: value = 7 changes to '7').

# 3. Return a new tree.

# ****  Look up early class demo with elegant code
def fizz_buzz(num):
    if not num % 15:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)

# def fizz_buzz_tree(self):
#     copy = Tree()
#     root = self.root
#     if root %15:
#        root.value = FizzBuzz
#         copy.root.value = FizzBuzz
#     elif root %3:
#        root.value = FizzBuzz
#         copy.root.value = Fizz
#     elif root %5:
#        root.value = Buzz
#         copy.root.value = Buzz
#    else:
#        root.value = FizzBuzz
#         copy.root.value = Fizz

#     def traverse
#       *** review code from tree implementation***