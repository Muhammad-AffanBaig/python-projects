contact_book = {}
while(True):
    print(" 1. Add Contact \n 2. Search Contact \n 3. Show All Contacts \n 4. Update Phone Number \n 5. Delete Contact \n 6. Count Contact Number \n 7. Exit")
    choice = int(input("Select your required choice: "))
    if(choice == 1):
        name = input("Enter your name: ").upper()
        number = input("Enter your contact number: ")
        contact_book[name] = number
        print("Your number is added successfully. Do press 2 to check your added phone number. Thank you!")

    elif(choice == 2):
        found = False
        name = input("Enter a name to find contact number: ").upper()
        for key in contact_book:
            if(name.lower()==key.lower()):
                found = True
                break
        if(found):
            print(name,"'s contact number:",contact_book.get(key))
        else:
            print("This person does not found")
    elif(choice==3):
        print("Here, we have all the contacts.")
        for key , value in contact_book.items():
            print(key,":",value)
    elif(choice ==4):
        found = False
        name = input("Enter your name: ").upper()
        for key in contact_book:
            if(name.lower() == key.lower() ):
                found = True
                break
        if(found):
            number = input("Enter number to update: ")
            contact_book[name] = number
            print("Your number is updated successfully. Do press 2 to check your updated phone number. Thank you!")
        else:
            print("This person does not found")
    elif(choice == 5):
        found = False
        name = input("Enter Your name: ").upper()
        for key in contact_book:
            if(name.lower() == key.lower() ):
                found = True
                break
        if(found):
            contact_book.pop(key)
            print("The contact is deleted.Do press 3 to check the contact list")
        else:
            print("This  person does not found")
    elif(choice==6):
        print("Total contact number:",len(contact_book))
    elif(choice==7):
        break    
    else:
        print("The choice is invalid.Do enter the appropriate choice.")