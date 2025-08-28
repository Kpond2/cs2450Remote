import random

def age_guesser():
    print("Hello! This is the age guesser. I will attempt to guess your age.")
    name = input("What is your name? ")

    while True:
        age = random.randint(15, 30)
        print("I guess your age is", age)
        answer = input("Is that correct? (y/n) ").lower()  
        if answer == "y":
            print(name + " is " + str(age) + " years old!")
            break
        else:
            print("Rats.")


age_guesser()
