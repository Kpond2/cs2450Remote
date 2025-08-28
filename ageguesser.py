import random

def age_guesser():
    print("Hello, This is the age guesser. I will attempt to guess your age.")
    name = input("What is your name?")
    age = random.randit(15, 30)  
    print("I guess your age is", age)
    answer = input("is that correct? (please respond with either y or n)")     

    if answer == "y":
        print(name + " is " + age + " years old.")  
    else:
        print("Rats.")
        print("I guess your age is", age)  
        answer = input("is that correct? (please respond with either y or n)")
        print("Rats")


print(age_guesser())  
