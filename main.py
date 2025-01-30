while True:
    response = input("What is the password?")

    if response == "abcd123":
        print("Good Job!")
        break
    else:
      
        response1 = input("Wrong, Would you like to try again? yes/no")
    
        if response1.lower() != "yes":
            print("Have a good day!")
            break
