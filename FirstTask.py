

from collections import Counter
import collections
number_list=[] # creates an empty list
n=int(input("Enter the number of words to be shown from the list: ")) #Takes integer input from user
for i in range(0,n):
    item = input()
    number_list.append(item) #Appends n number of items in number_list by using for loop
word = number_list 
occurrences = collections.Counter(word) #This counts the number of occurences a word has occur in the list
occurrences = dict(occurrences) #occurences gets casted into dictonaries where word is key and number of times it occurs is it's value
print(occurrences) #Print the number of times a word is repeated
word = set(word) # Typecasted in set from list
a = len(word) #print the number of distinct elements
print(f"The number of distinct words are {a}")





