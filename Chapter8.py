from random import randint
from _ast import Num

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
print (random_number)

guesses_left = 3

while guesses_left != 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print 'You win!'
        break
    guesses_left -= 1
else:
    print "You lose."
##########################
hobbies = []

for x in range(3):
    hobby = raw_input("Enter hobby: ")
    hobbies.append(hobby)
##########################
phrase = "A bird in the hand..."

for char in phrase:
    if char == 'A' or char == 'a':
        print 'X',
    else:
        print char,
        
print()
##########################
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry', 'd': 'pussy'}

for key in d:
    print key, d[key]
    
############################
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index + 1, item
############################
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a >= b:
        print a
    else:
        print b
######################For/else8.17
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'
##################is_even8.18.2
def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False
###########################8.18.3
def is_int(x):
    if x >=0 or x<0:
        if round(x)-x == 0:
            return True
        else:
            return False
    else:
        return False

print is_int(3.4)
###########################8.18.4
def digit_sum(n):
    digits = []
    while n:
        mod10 = n%10
        digits.append(mod10)
        n = (n - mod10)/10
    return sum(digits)
        
digit_sum(1234)

##OR
def digi_sum(n):
    numbers = []
    n = str(n)
    for char in n:
        numbers.append(int(char))
        numsum = sum(list(numbers))
    print numsum
    
digi_sum(1234)
############################8.18.5
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print factorial(3)
############################8.18.6Prime Numbers
def is_prime(x):
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False
    
print (is_prime(9))
###########################8.18.7
def reverse(text):

    lst = []
    count = 1

    for i in range(0,len(text)):

        lst.append(text[len(text)-count])
        count += 1

    lst = ''.join(lst)
    return lst

print reverse('Whore')
############################8.18.8
def anti_vowel(text):
    txt = ""
    for c in text:
        if c not in "aeiouAEIOU":
            txt += c
    return txt
##############################8.18.9 Scrabble Score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    for letter in word.lower():
        total += score[letter]
    return total

print scrabble_score("Whore")
##################################8.18.10 Censors
text= 'Love thy neighbor'
word = 'thy'

def censor(text, word):
    return text.replace(word, '*'*len(word))

print censor(text, word)
##################################8.18.11 count
def count(sequence, item):
    counter = 0
    for number in sequence:
        if number == item:
            counter += 1
    return counter

print count([1,2,1,1], 1)
#################################8.18.12 pufify
def purify(numbers):
    new_list = []
    for num in numbers:
        if num%2 == 0:
            new_list.append(num)       
    return new_list

print purify([1,2,3,4,5,6,7,8,9,10])
################################8.18.13 product
def product(numList):
    total = 1
    for num in numList:
        total *= num 
    return total

print product([4, 5, 5])
###################################8.18.14 remove duplicates
def remove_duplicates(myList):
    newList = []
    for num in myList:
        if num not in newList:
            newList.append(num)
    return newList

print remove_duplicates([1,1,2,2,3,4,5,5,6,6])
####################################8.18.15 median
def median(myList):
    myList = sorted(myList)
    l = len(myList)
    if l % 2 == 0:
        return (myList[l/2-1] + myList[l/2])/2.0
    else:
        return myList[(l-1)/2]    
    

print "Median is " + str(median([2,8,1,5,3]))

    
    
    
        


    

    