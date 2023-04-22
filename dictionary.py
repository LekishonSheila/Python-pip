fruits = ["mango","banana","apple"]
fruits.append("avocado")
print(fruits)
fruits2 = ["pawpaw","orange","passion"]
fruits.extend(fruits2)
print(fruits)
fruits.insert(0,"berries")
print(fruits)
# school("AkiraChix")
print(1,"e")
fruits.sort()

# Create a student dictionary and add first_name, last_name,
#  gender, age, marital status, skills, country, 
# city and address as keys for the dictionary
# Get the length of the student dictionary
# Get the value of skills and check the data type, it should be a list
# Modify the skills values by adding one or two skills

# create a dictionary for a student
student = {
    "first_name": "Sheila",
    "last_name": "Lekishon",
    "gender": "Female",
    "age": 20,
    "marital status": "Single",
    "skills": ["Python", "Java", "KOtlin"],
    "country": "Kenya",
    "city": "Nairobi",
    "address": "123 Kilgoris"
}

# get the length of the student dictionary
length = len(student)
print("Length of student dictionary:", length)

# get the value of skills and check data type
skills = student["skills"]
print("Type of skills:", type(skills))

# modify the skills values by adding one or two skills
student["skills"].append("JavaScript")
student["skills"].append("HTML/CSS")

# print the updated dictionary
print(student)
