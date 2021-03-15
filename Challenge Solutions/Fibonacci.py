a = 1
b = 1
print(a)
print(b)

# will stop after 100 repeats
for i in range(100):
    c = a + b

    a = b
    b = c
    print(c)