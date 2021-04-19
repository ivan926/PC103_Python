firstName = input("Please type your first name: ")

lastName = input("Please type your last name: ")

emailAddr = input("Please type your email address: ")

phoneNumber = input("Please type your phone number: ")

jobTitle = input("Please type your current job title: ")

idNumber = input("Please type your ID number: ")

hairColor = input("Please type your hair color: ")

eyeColor = input("Please type your eye color: ")

startMonth = input("Please type month that you started working: ")

advTraining = input("Have you recieved advanced training (type yes or no): ")

#Below is the printed variables along with 
#the proper functions appended

print("The ID Card is: ")

print("-------------------------------")

print(lastName.upper() + ", " + firstName)

print(jobTitle.capitalize())

print("ID: {0}".format(idNumber))

print()

print(emailAddr.lower())

print(phoneNumber)

print()

print(f"{'Hair: ' + hairColor.capitalize():<25} Eyes: {eyeColor.capitalize()}")

print(f"{'Month: ' + startMonth.capitalize():<25} Training: {advTraining.capitalize()}")

print("-------------------------------")