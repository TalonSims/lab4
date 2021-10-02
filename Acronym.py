def main():

    user_string = input("Enter a multi-word phrase: ")
    acronym = user_string[0].upper()                    # First letter
    for i in range (len(user_string)):
        if user_string[i] == " ":
            acronym = acronym + user_string[i + 1].upper()  # Uppercase initials by each word
    print ("Your acronym: ", acronym)

if __name__ == "__main__":
    main()

    
