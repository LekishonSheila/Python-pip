# I am a teacher and I love to inspire and teach people. How many unique words 
# have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split() 
unique_words = set(words) 
print(len(unique_words)) 

# # sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add('Twitter')
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.remove('Oracle')
print(it_companies)


