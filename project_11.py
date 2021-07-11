
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]


youngest_age = 100
youngest_person_name = ""

for youngest_person in people:

    list_of_names = youngest_person.split(" ")
    
    if int(list_of_names[1]) < youngest_age:

        youngest_age = int(list_of_names[1])
        youngest_person_name = list_of_names[0]
   


print(f"The youngest person is {youngest_person_name}, and he is {youngest_age} years old.")