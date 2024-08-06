import datetime

def calculate_year_100 ():
    print("What's your name?")
    name = input()
    print("Welcome "+name+". What's your age?")
    age = int(input())
    date = int(datetime.datetime.now().strftime("%Y"))
    future = date - int(age) + 100
print("You will be 100 years old in "+future)

calculate_year_100()