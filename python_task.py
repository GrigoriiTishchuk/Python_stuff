def assign():
    var = 5
    print(var)

assign()




def choice(bol: bool):
    if bol:
       print("HERE IS FIRST ONE")
    else:
       print("HERE IS SECOND ONE")

boli = False

choice(boli)



def upper(string: str):
    print(string.upper())

string = input("Enter string: ")

upper(string)


def square_and_root(num):
   return {"square": num**2, "root": num**0.5}


num = int(input("Enter number: "))

print(square_and_root(num))


lst = [1,2,3,4,5]

for item in lst:
    print(lst[item-1])


def custom_sum(lis):
    total = 0
    for item in lis:
        total += item
    return total

print("Custom sum: ",custom_sum(lst))

dic = { 
    "first": 26,
    "Second": 32 
}

def mult(dii: dict):
    total = 1
    vals = dii.values()
    for item in vals:
        total *= item
    return total


print("Hre is osm: ",mult(dic))


def sheesh(some: int):
    return lambda sus: ["IT IS OVER 9000" if sus * some > 9000 else "Usuall: ", sus * some]

doubler = sheesh(4000)

print("Cac: ", doubler(2))
