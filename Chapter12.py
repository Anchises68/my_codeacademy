my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()
#You can open files in write-only mode ("w"), read-only mode ("r"), 
#read and write mode ("r+"), and append mode ("a", which adds any 
#new data you write to the file to the end of the file).
# 4. Reading 
#print f.read() -- can't actually perform, needs an actual file'
# 8. 
with open("text.txt", "w") as textfile:
    textfile.write("Success!")