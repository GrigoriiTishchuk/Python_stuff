mult = lambda a, b: a * b
divi = lambda a, b: a / b
exp = lambda a, b: a ** b

print(mult(2, 3))
print(divi(6, 2))
print(exp(10, 3))

#func with lambda
def double (x):
    return lambda a: a * x

doubler = double(2)

print(doubler("sus"))

#sort the list of strings
list = ["asdasd", "gfsd", "sdf", "asdfgghbfgdb", "q"]

sorter = lambda x: sorted(x, key=len)

print(sorter(list))

#CHANGE CamelCase to kebab-case
def camel_to_kebab (x):
    kebab_string = ""
    for i, char in enumerate(x):
        if i == 0:
            kebab_string += char.lower()
        elif char.isupper():
            kebab_string += "-" + char.lower()
        else:
            kebab_string += char

    return kebab_string

CamelCase = input("Enter a CamelCase: ")

print(camel_to_kebab(CamelCase))


#doubler of every number in array
array = [123, 256, 21, 3, 47, 11]

doubl = lambda arrx: [x * 2 for x in arrx]

print(doubl(array))