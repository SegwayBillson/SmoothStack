import random

for i in range(1500,2701):
    if(i % 7 == 0 and i % 5 == 0):
        print(i)

def temp_convert(temp, temp_val):
    if(temp.lower() == 'c'):
        print(float(temp_val)*(9/5)+32)
    elif(temp.lower() == 'f'):
        print((float(temp_val)-32)*(5/9))
    else:
        print("please enter C or F for first value")

temp_convert(input("Specify current temperature unit (C or F): "), input("Enter current temperature: "))

def num_guess():
    print("I thought of a random number 1-9!")
    secret_num = random.randint(1,9)
    guess = 0
    while(secret_num != guess):
        guess = int(input("Enter a number to guess: "))
        if(guess != secret_num):
            print("Wrong!")
    print("Well guessed!")

num_guess()


def sideways_pyramid():
    row = []
    for seq in range(2):
        if (seq == 0):
            for x in range(5):
                row.append('*')
                print(" ".join(row)) 
        else:
            for x in range(4):
                row.pop(0)
                print(" ".join(row))

sideways_pyramid()


def rev_word(word):
    return word[::-1]

print(rev_word(input("Enter a word to reverse: ")))

def count_odd_even(numbers):
    odd = 0
    even = 0
    for num in numbers:
        if(num % 2 == 0):
            even += 1
        else:
            odd+=1
    print("Number of even numbers: " + str(even))
    print("Number of odd numbers: " + str(odd))

count_odd_even((1,2,3,4,5,6,7,8,9))

def print_type(lst):
    for thing in lst:
        print(str(thing) + ", " + str(type(thing)))

print_type([1452, 11.23, '1+2j', True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}])

def skip_3_6():
    for i in range(7):
        if(i == 3 or i == 6):
            continue
        print(i)

skip_3_6()