roster = ["Adam","Alex","Mariah","Martine","Columbus"]
for name in roster:
    print name
    
#############  
webster = {
    "Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

for key in webster:
    print webster[key]
############    
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
    if number % 2 == 0:
        print number
##############
def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count  += 1
    return count
            
print fizz_count(["fizz", "fizz", "fizz"])
##################
prices = {"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

stock = {"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}

for key in prices:
    print key
    print "Price: %s" % prices[key]
    print "Stock: %s" % stock[key]
    
total = 0
for item in prices:
    print item
    print prices[item] * stock[item]
    total += prices[item] * stock[item]
    print "Total: " + str(total)
######
######Day at the Supermarket - this one was a bitch
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] = stock[item] - 1     
    return total
 
print "Total bill: " + str(compute_bill(shopping_list))
print stock
######################
###Student Becomes Teacher - https://www.codecademy.com/courses/python-beginner-en-qzsCL/1/4?curriculum_id=4f89dab3d788890003000096

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
    
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
    
students = [lloyd, tyler, alice]

def average(numbers):
    total = sum(numbers)
    
    return float(total)/len(numbers)

def get_average(student):
    homework = student["homework"]
    quizzes = student["quizzes"]
    tests = student["tests"]
    return .1 * average(homework) + .3 * average(quizzes) + .6 * average(tests)

def get_letter_grade(score):
    if score >= 90.0:
        return "A"
    elif score >= 80.0:
        return "B"
    elif score >= 70.0:
        return "C"
    elif score >= 60.0:
        return "D"
    else:
        return "F"
        
def get_class_average(students):
    results = []
    for grade in students:
        results.append(get_average(grade))    
    return average(results)
    
print "Class Average: " + str(get_class_average(students))
print "Class Letter Grade: " + get_letter_grade(students)
##############################################################
n = [2, 4, 6]
n.pop(1)
print n
m = [1, 3, 9]
m.remove(3)
print m
k = [5, 7, 8]
del(k[1])
print k
###############################################################
n = [3, 5, 7]

def print_list(x):
    for i in range(0, len(x)):
        print x[i]
         
print_list(n)

n = [3, 5, 7]

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print double_list(n)
###############################################################
def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print "Range: " + str(my_function(range(0,3,2)))

n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
    return result

print "Range addition total: " + str(total(n))

m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x,y):
    result = x + y
    return result

print join_lists(m, n)

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
    results = []
    for numbers in lists:
        results += numbers
    return results

print flatten(n)
#########################################
my_shit = range(0,100,3)
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes", "pussy", "tits", "ass", "thighs", "nipples", "clitoris"]
def some_function(xyz):
    some_list = []
    for i in range(0, len(xyz)):
        some_list.append(xyz[i:i+3])
    return some_list

print (some_function(suitcase))



        
        
        


    
     
        
        
        