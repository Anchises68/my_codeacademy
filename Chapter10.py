my_dict = {
    "Tits": 36,
    "Waste": 24,
    "Ass": 40
    }

print (my_dict)
print (my_dict.items())
print (my_dict.keys())
print (my_dict.values())

for key in my_dict:
    print (key, my_dict[key])
    
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print ("evens_to_50: " + str(evens_to_50))

doubles = [x*2 for x in range(1,6)]
print ("doubles: " + str(doubles))

new_list = [x for x in range(1,6)]
print ("new_list: " + str(new_list))

doubles_by_3 = [x*2 for x in range(1,12) if (x*2) % 3 == 0]
print ("doubles_by_3: " + str(doubles_by_3))

even_squares = [x**2 for x in range(1,11) if x % 2 == 0]
print ("even_squares: " + str(even_squares))

cubes_by_four = [x**3 for x in range(1,11) if x**4 % 4 == 0]
print ('cubes_by_four: ' + str(cubes_by_four))

#7. List test_slicing
l = [i ** 2 for i in range(1, 11)]
print (l[2:9:2])

my_list = range(1, 101)
print (my_list[::2])

backward = my_list[::-2]
print ("my_list backward: " + str(backward))

to_21 = range(0,22)
odds = to_21[1::2]
print ("odds: " + str(odds))

to_21 = range(0,22)
odds = to_21[1::2]
middle_third = to_21[8:15:]
print ("middle_third: " + str(middle_third))

#12. Lambda
my_list = range(16)
print (filter(lambda x: x % 3 == 0, my_list))

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print (filter(lambda x: x == "Python", languages))

squares = [x**2 for x in range(1,11)]
print (filter(lambda x: x <=70 and x >= 30, squares))
#15. Iterating of dicitionaries
movies = {
    "Monty Python and the Holy Grail": "Great",
    "Monty Python's Life of Brian": "Good",
    "Monty Python's Meaning of Life": "Okay"
}

print (movies.items())
#16. Comprehension
threes_and_fives = [x for x in range(15) if x % 3 == 0 or x % 5 == 0]
print (threes_and_fives)

#18.
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != "X", garbled)
print (message)
#Bitwise Operators
print (5 >> 4)  # Right Shift
print (5 << 1)  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT
#2.
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11
#3.
print "Section 3"
print (0b1)
print (0b10)
print (0b11)
print (0b100)
print (0b101)
print (0b110)
print (0b111)
print (0b1000)
print (0b1001)
print (0b1010)
print (0b1011)
print (0b1100)
#4.
print ("100 as binary: ")
print (bin(100))
#5.
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001", 2)
#6. Bitwise Operator
shift_right = 0b1100
shift_left = 0b1

print ("shift_right before: " + str(int(bin(shift_right), 2)))
print ("shift_left before: " + str(int(bin(shift_left), 2)))
# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print ("shift_right after: " + str(int(bin(shift_right), 2)))
print ("shift_left after: " + str(int(bin(shift_left), 2)))
#7. Bit AND
print bin(0b1110 & 0b101)
#8. Bit OR
print int(bin(0b110), 2)
print int(bin(0b101), 2)
print int(bin(0b1110 | 0b101), 2)
#8. Bit XOR
print int(bin(0b1110 ^ 0b101), 2)
#11
print int(bin(0b1100), 2)
print int(bin(0b0100), 2)
num  = 0b1001
mask = 0b0101
desired = num & mask
if desired > 0:
    print "Bit was on"
    
def check_bit4(num):    
    mask = 0b1000
    if num & mask > 0:
        return 'on'
    else:
        return 'off' 
    
check_bit4(1)
print int(bin(0b1), 2)

#12.
a = 0b10111011
mask = 0b100
desired = a | mask
print bin(desired)

#13.
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print bin(desired)

#14.
def flip_bit(number, n):
    mask = 0b1 << (n-1)
    result = number ^ mask
    return bin(result)  

