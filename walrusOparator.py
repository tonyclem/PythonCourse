a = 'helloooooworld'

if (n := len(a)) > 10:
    print(f"to long {n} elements")

while(( n := len(a)) > 1):
    # print(n)
    a = a[:-1]
print(a)

# nonlocal variables
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

# global variables
total = 0
def count():
    global total
    total += 1
    return total
print(count())

total = 0
def count(total):
    total += 10
    return total
print(count(total))

