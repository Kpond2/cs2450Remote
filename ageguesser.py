import random

def age_guesser():
    print("Hello, This is the age guesser. I will attempt to guess your age.")
    name = input("What is your name?")

    age = random.randint(15, 30)

    print("I guess your age is", age)
    answer = input("Is that correct? (y/n)")

    if answer == "y":
        print(name + " is " + age + " years old.")
    else:
        print("Rats.")
        print("I guess your age is", str(age)
        answer = input("Is that correct? (y/n)")
        print("Rats")
age_guesser()
