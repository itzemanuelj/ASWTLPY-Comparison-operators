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

