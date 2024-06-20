from random import randint

num1 = int(input("enter your first number"))
num2 = int(input("enter your second number"))
num3 = int(input("enter your third number"))

gen1 = randint(0, 9)
gen2 = randint(0, 9)
gen3 = randint(0, 9)

print(f"user input: {num1}{num2}{num3}")
print(f"generated numbers: {gen1}{gen2}{gen3}")

if [num1, num2, num3] == [gen1, gen2, gen3]:
    print("you win")
else:

    if sorted ([num1, num2, num3]) == sorted([gen1, gen2, gen3]):
        print("you partially win")
    else:
        print("you lose")