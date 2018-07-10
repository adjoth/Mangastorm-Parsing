import os

#Importing Classes
from mangaClass import Manga as Manga

file = open("favorites.msbf", "r")                  # Opens file (Remember to close when finished)

for line in file:
    print(line.split('\t'))


#with open("favorites.msbf", "r") as file:           # Opens file and closes when end of function
#    print(file.read(5))

#print(file.read())          # Reads entire files
#print(file.read(5))         # Reads characters from 0-5 (6 total) including whitespace
#print(file.readline())      # Reads untill return character
#print( file.readline(16))   # Functions as read(x)
#print(file.readlines())     # **WARNING: CRASHES** In theory will return each line as a seperate sting **WARNING: CRASHES**

# Print lines in a loop
##for line in file:
##    print(line)
##    break                 # Breaks after first line

# Reading in specific lines [TEST 01 METHOD 01]     ** FAILED **
# TypeError: 'in <string>' requires string as left operand, not int
##i = 1
##for line in file:
##    if i in line:
##        print(i)  # swaping with line still fails
##    i+=1


# Reading in secific lines [TEST 01 METHOD 02]      ** SUCCESS  [TEST CLEARED]**
# Method Reads line one-by-one
##print(file.readline())
##print(file.readline())

# Reading in a line using .split()  [TEST 02 METHOD 01]     ** PARTIAL SUCESS **
# Reads in lines and saves 2nd line too data, however cannot split
##print(file.readline())
###data = file.readlines()         # Saves last line as data then splits as words, may also result as infinite if not used with .split()
##data = file.readline()
##for lines in data:
##    #print(lines)                # Prints each character
##    words = lines.split()
##print(words)                    # Returns null list
###print(data)

# Reviewing METHOND 01 [TEST 02 METHOD 01]
##dummy = file.readline()
##data = file.readline()
##words = []      # Empty Array to test scope ** FAILED **
##print(data)                     # Prints 2nd line
##for l in data:
##    words = l.split()        # if any string is placed in () results in \n value returned, otherwise empty
##    print(words)                # Retuns each character '\t' shows up as whitespace between words [REQUIRES FURTHER TESTING]
##print(words)

# Trying split methond using '\t' as condition  [TEST 02 METHOD 02]
##line = "----------------------------------------------\n"
##print(file.readline())
##data = file.readline()
##print(line,data,line)
##for lines in data:
##    words = lines.split("")
##print(words)                    # Still retuns '\n' [Scope? = No]

# Trying split fucntion with user value [TEST 02 METHOD 03]    ** SUCCESS **
##x = "Red,Blue,Green"
##a,s,d = x.split(",")
##print(a)

# Expanding method 03 [TEST 03 METHOD 04]       ** SUCESSS **
# Each word is sepearted correclty by '\t'
##x = "Hello\tWorld\tThis\tis\tit"
##y = x.split('\t')
##print(y)

# Reviewing Method 02 without for funtion   [TEST 02 METHOD 05]     ** SUCESS [TEST CLEARED] **
# Sperates line into list by '\t' character. Doesn't seperate anything that shouldn't be seperated
##dummy = file.readline()
##data = file.readline()
##words = data.split('\t')
##print(words)
file.close()
