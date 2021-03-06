# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 
# 7:50pm start
def tax_calculator(state, item_cost, tax_percentage = 0.05):
    if state == 'CA':
      tax_percentage = 0.07
    total = item_cost*tax_percentage + item_cost
    return total
# 7:57 end
#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

def is_berry(fruit_name):
  is_true = False
  if fruit_name in ['strawberry', 'cherry', 'blackberry']:
    is_true = True
  return is_true
# 8:03 end
# commit
#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.
def shipping_cost(fruit_name):
  if is_berry(fruit_name) == True:
    return 0
  else:
    return 5
# 8:08
# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
def is_hometown(town_name):
  is_home = False
  if town_name in ['San Jose', 'San Francisco', 'Cupertino']:
    is_home = True
  return is_home
# 8:10
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
def full_name(first_name, last_name):
  return first_name + ' ' + last_name
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.
def hometown_greeting(hometown_name, first_name, last_name):
  if is_hometown(hometown_name) == True:
    print "Hi " + full_name(first_name, last_name) + ", we're from the same place!"
  else:
    print "Hi " + full_name(first_name, last_name) + ", where are you from?"
# 8:18



#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.
def increment(x):
  x = 1
  def add(y):
    return x+y 
  return add

# ?
# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20. 
#    
addfive = increment(5)
addfive(5)
addfive(20)
# 8:41
# ??
# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.
def add_last(number, number_list):
  number_list.append(number)
  print number_list
# 8:33
#####################################################################