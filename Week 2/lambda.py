numbers = [1, 2, 3, 4, 5]
def doubleit(x):
    return x**2;
ok=map(doubleit,numbers)
print(list(ok))