# IF ELSE ELIF 
print('What is age?')
age = int(input('number:')) # user gives number as input
if age > 18:
    print('go ahead drive')
elif age == 18:
    print('come personaly for test')
else:
    print('still underage')


species = "cat"
if species == "cat":
  print("Yep, it's cat.")
else:
    print("Nope, not cat.")

# If the condition tested in line 1 fails, line 3 tests for a different condition. What keyword goes in the blank?
donut_condition = "fresh"
donut_price = "low" 

if donut_condition == "fresh":
    buy_score = 10
elif donut_price == "low":
    buy_score = 5
else:
    buy_score = 0

# Code the next line that says what to do if the test fails.
a = 1
b = 10

if a == b:
   print("a equals b")
elif a != b:
    print("a doesnt equal b")

# Code the next line. If a doesn't equal b, test whether c equals d.
c = 1
d = 10
if a == b:
   print("a equals b")
elif c == d:
    print("c equals d")
else:
    print("a,b,c,d are unequal")

# Code four lines. If a equals b, c equals d. If the test fails, e equals f.
f = 1

if a == b:
  c = d
else:
  e = f

# Code four lines. If a equals b, c equals d. If that test fails, then if e equals f, g equals h.
h = 10
if a == b:
    c = d
    print()
else:
    e = f  
    g = h

# What is the value of x?
if 2 + 3 == 4:
  x = 0
elif 2 - 1 == 1:
  x = 1
elif 3 + 3 == 6:
  x = 2
else:
  x = 3

# x is equal to 1

# Code the next two lines. If the test fails, test if a equals 2. If so, display "a equals 2".
a = 1
if a == 1:
  print("a equals 1")
elif a == 2:
    print("a equals 2")

# Code the next two lines. If the first two tests fail, display "failed".

if a == b:
  print("ok")
elif c == d:
  print("ok")
else:
    print("failed")

# Code six lines. If a equals b, display "ok". If not, then if c equals d, display "ok". If both tests fail, display "failed".
if a == b:
    print("ok")
elif c == d:
    print("ok")
else:
    print("failed")

if "dog" == "cat":
  print ("That's crazy")
else:
    print("wrong")

# On the next two lines, display "wrong" if the condition isn't met.
# Display wrong if the condition isn't met.
# If the first condition isn't met, test whether "cat" equals "cat." If so display ok

if "dog" == "cat":
  proposition = "crazy"
else:
    print("ok")
# On the next two lines, if the condition above isn't met,
# test whether "cat" is equal to "cat"
# If so, display "ok"
# If the first condition isn't met, test whether "cat" equals "cat." If so display ok

  
  
