import functools

#~~~~~~~~~~~~~~Day 4 a~~~~~~~~~~~~~~~

def func():
    print('Hello World')

#func()

def func1(name):
    print('Hi my name is ' + str(name))

#func1("Doug")

def func3(x,y,z):
    if(z):
        return x
    return y

#print(func3('Hello','Goodbye',False))
#print(func3('Hello','Goodbye',True))

def func4(x,y):
    return x*y

#print(str(func4(2,3)))

def is_even(num):
    return num % 2 == 0

#print(is_even(2))
#print(is_even(3))

def num_comp(x,y):
    return x>y

#print(num_comp(2,3))
#print(num_comp(3,2))
#print(num_comp(2,2))

def sum_up(*argv):
    sum = 0
    for num in argv:
        sum += num
    return sum

#print(sum_up(2,2,2))

def even_only(*argv):
    return [x for x in argv if x % 2 == 0]

#print(even_only(1,2,3,4,5,6,7,8,9))

def upper_lower(word):
    answer = ""
    for char in range(len(word)):
        if(char % 2 == 0):
            answer += word[char].upper()
        else:
            answer += word[char].lower()

    return answer

#print(upper_lower("Hello World"))

def num_comp2(x,y):
    if(x % 2 == 0 and y % 2 == 0):
        return min(x,y)
    return max(x,y)

#print(num_comp2(1,2))
#print(num_comp2(2,4))
#print(num_comp2(1,3))

def match_first(word1, word2):
    return word1[0] == word2[0]

#print(match_first("Hello","world"))
#print(match_first("Doug","Dog"))

def square(x):
    return x**2

#print(square(7))

def specific_cap(word):
    lst = list(word)
    lst[0] = lst[0].upper()
    lst[3] = lst[3].upper()
    return "".join(lst)

#print(specific_cap("hello world"))

#~~~~~~~~~~~~~~Day 4 b ~~~~~~~~~~~~~~~

def price_calc(lst):
    return list(map(lambda x: ( x[0], (x[2] * x[3]) + (10 if x[2] * x[3] <= 100 else 0)), lst))

    
def price_calc2(lst):
    return list(map(lambda x: ( x[0], functools.reduce(lambda a,b: a + (b[1]*b[2]), x) - x[0]),lst))

print(price_calc2([[1,[1,2,10],[2,5,5]],[2,[3,3,11],[2,12,2]]]))
