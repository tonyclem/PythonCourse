# Conditional Logic

is_old = False
is_license = True

if is_old:
    print("you\'re, good to go!")
elif is_license:
    print("you can drive now!")
else:
    print("so you can\'t drive")
print("good to go!")

# Example II Short Hand if Else
a = 2
b = 330
print('lower') if a > b else print('higher')

# Ternary Operators
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Example II 
is_today_weekend = True
can_be_weekend = "Yes todays is weekends" if is_today_weekend else "No todays is\'nt weekend"
print(can_be_weekend)

# And Conditional Operators
is_today_christmas_eve = True
is_today_christmas = False

if is_today_christmas and is_today_christmas_eve:
    print("yeah is wonderful day, so let enjoy!")
else:
    print("Sorry tomorrow is awesome because it's christmas day, so let enjoy!")

# Short Circuit
is_friend = 0
is_user = False

if is_friend or is_user:
    print("best friend forever")
else: 
    print("Sorry is\'nt a friend")

# Exercise 
is_magician = False
is_expert = True

# Ternary answers

if is_magician and is_expert:
    print("you are a master magician")
elif is_magician and not is_expert:
    print("at least you\'re getting there")
elif not is_magician:
    print("you need magic Power")

# print("you are a master magician") if is_magician and is_expert else print("at least you\'re getting there") if is_magician or is_expert else print("you need magic Power")
print(True is True) # Truthy
print('' == 1) # Falsy
print([] == 1) # Falsy
print(10 == 10.0) # True
print([] is []) # False

a = [1,2,3] 
b = [1,2,3] 
print( a is a)
