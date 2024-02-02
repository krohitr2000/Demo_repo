#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SCS
#
# Created:     16-08-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0]=='s':
        print(word)


# Use range() to print all the even numbers from 0 to 10.
even_numbers=[num for num in range(0,10) if(num%2==0)]
print(even_numbers)


#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
mylist=[num for num in range(1,50) if(num%3==0)]
print(mylist)


# Go through the string below and if the length of a word is even print "even!"
new_st = 'Print every word in this sentence that has an even number of letters'
for word in new_st.split():
    n= len(word)
    if (n%2==0):
        print(word)

# Use a List Comprehension to create a list of the first letters of every word in the string below:
stnew = 'Create a list of the first letters of every word in this string'
newlist=[word[0] for word in stnew.split()]
print(newlist)
