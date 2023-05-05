# Write a python function named divisible_by_seven that;using the range function and a for loop returns
# a list containing all the numbers between between 100 and 200 taht are divisible by seven
def divisible_by_seven():
    x=range(100,200)
    empty=[]
    for i in x:
        if(i % 7==0):
            empty.append(i)
            return empty
    print(divisible_by_seven) 

# while loop to print prime numbers from 1 to 10
def PrimeNum(num):
    if num <2:
        return False
    for i in range(2,num):
        if (num%i==0):
            return False
    return True
num=0
while(num<=10):
        if PrimeNum(num):
            print(num)
        num+=1  
# Define a function that accepts a string as input and uses the for loop to iterate through
# the string and count the vowels
def count_vowel(vowels):
    # name = "Lekishon sheila"
    count=0
    vowels["a","e","i","o","u"]
    for vowel in vowels:
        if vowel in vowels:
            count+=1
    return count

print(name("Lekishon sheila"))



     
        
