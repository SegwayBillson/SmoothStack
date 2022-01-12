# ~~~~~~~~~~~~~Day_2_a~~~~~~~~~~~~~~~~~

print('Hello World'[8])

print('thinker'[2:5])

print('hello'[1])

print('Sammy'[2:])

print(set("Mississippi"))

def palindrome(phrases):

    lines = phrases.lower().split('\n')
    answer = ""

    for line in range(1,len(lines)):

        # Remove all non-letter characters from the line
        i_line = ''.join(e for e in lines[line] if e.isalnum())
        steps = (len(i_line)//2)

        for c in range(steps):
            if(i_line[c] != i_line[len(i_line)-c-1]):
                answer = answer + "N "
                break
            elif(c == steps-1):
                answer = answer + "Y "
    return answer[:-1]

print(palindrome("3\nStars\nO, a kak Uwakov lil vo kawu kakao!\nSome men interpret nine memos"))

# ~~~~~~~~~~~~~Day_2_b~~~~~~~~~~~~~~~~~

print((10,"word",0.1))

nest_list = list((1,1,(1,2)))

print(nest_list[2][1])

lst = ['a','b','c']

print(lst[1:])

weekdays = {"Monday" : 1, "Tuesday" : 2, "Wednesday" : 3, "Thursday" : 4, "Friday" : 5, "Saturday" : 6, "Sunday" : 7}

print(weekdays)

d = {'k1' : [1,2,3]}

# Throws Error
#print(d[k1][1])
print(d['k1'][1])

t_list = (1,(2,3))

print(tuple(t_list))

ms = "Mississippi"
ms = set(ms)

print(ms)

ms.add('X')

print(ms)

print(set([1,1,2,3]))

# Question 1

answer = ""
for x in range(2000,3201):
    if(x % 7 == 0 and x % 5 != 0):
        answer += (str(x) + ',')
print(answer[:-1])

# Question 2

def fact(x):
    if(x == 0):
        return 1
    return x * fact(x-1)

x = int(input("Enter number for factorial: "))
print(fact(x))

# Question 3

def squares(x):
    d=dict()
    for i in range(1,x+1):
        d[i]=i*i	
    print(d)

s_value = int(input("Enter single integer: "))
squares(s_value)

# Question 4

def list_and_tuple():
    nums = input("Enter comma seperated values: ")
    nums = nums.split(',')
    print(nums)
    print(tuple(nums))

list_and_tuple()

# Question 5

class StrClass():

    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input("Enter new string: ")
    def printString(self):
        print(self.s.upper())

str_obj = StrClass()
str_obj.getString()
str_obj.printString()

# ~~~~~~~~~~~~~Day_2_c~~~~~~~~~~~~~~~~~
def three_is_a_crowd():
    def crowd_test(lst):
        if(len(lst) > 3):
            print("The room is crowded")

    print("Three is a Crowd Pt")

    people = ["Steve","Doug","Hannah","Jeremiah"]

    crowd_test(people)

    people.pop(0)
    people.pop(0)

    crowd_test(people)

three_is_a_crowd()

def three_is_a_crowd_pt2():
    def crowd_test(lst):
        if(len(lst) > 3):
            print("The room is crowded")
        else:
            print("The room is not crowded")

    print("Three is a Crowd Pt 2")

    people = ["Steve","Doug","Hannah","Jeremiah"]

    crowd_test(people)

    people.pop(0)
    people.pop(0)

    crowd_test(people)

three_is_a_crowd_pt2()

def six_is_a_mob():
    def crowd_test(lst):

        if(len(lst) > 5):
            print("There's a mob in this room")
        elif(len(lst) > 3):
            print("The room is crowded")
        elif(len(lst) > 1):
            print("The room is not crowded")    
        else:
            print("The room is empty")

    print("Six is a Mob")

    people = ["Steve","Doug","Hannah","Jeremiah","Ozzy","Kody"]

    crowd_test(people)

    people.pop(0)
    people.pop(0)

    crowd_test(people)

six_is_a_mob()
