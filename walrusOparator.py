a = 'helloooooworld'

if (n := len(a)) > 10:
    print(f"to long {n} elements")

while(( n := len(a)) > 1):
    # print(n)
    a = a[:-1]
print(a)
