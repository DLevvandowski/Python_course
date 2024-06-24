# This is the first approach in terms of how to import a module. It simply involves using the import command and
# specifying the module name. This will make all the functions in the module available to the current program.

import pizza

pizza.make_pizza(40, 'pepperoni')
pizza.make_pizza(30, 'mushrooms', 'green paprica', 'double cheese')

# When we want to import only the function we will use, then the import command will be of the following form:
#
#   from name_module import name_function_0, name_function_1
#
# With this syntax, you do not need to use dot notation when calling a function.

from pizza import make_pizza

make_pizza(40, 'pepperoni')

# When the name of an imported function may conflict with the name of a function already existing in the program, or
# this name is too long, then a shortcut can be used. The abbreviation in question is a unique alias, or alternative
# name, much like a nickname for a function. This special nickname is given to the function when it is imported. The
# general syntax to create an alias is as follows:
#
# from name_module import name_function as alias

from pizza import make_pizza as mp

mp(50, 'ham', 'cheese')

# it is also possible to create an alias for the module name. Giving a module a short alias, for example p for pizza,
# allows you to call module functions even faster. The general syntax to create an alias for a module is as follows:
#
# import name_module as alias

import pizza as p

p.make_pizza(30, 'cheese')

# Using the * operator, you can command Python to import all the functions contained in a module. I mentioned the import
# command appearing together with an asterisk only because you may encounter this solution when analyzing code created
# by other programmers:
#
# from name_module import *

from pizza import *
make_pizza(25, 'chilli')
