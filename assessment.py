choice = input("Do you like platformers or shooter games?")
if choice == "Platformers":
    choice2 = input("Do you like the badguys to be aliens or mushrooms")
    if choice2 == "aliens":
        print("I recommend Metroid!")
    elif choice2 == "mushrooms":
        print("I recommend Mario Bros")
    else:
        print("That's not a choice")
elif choice == "Shooter":
      choice2 = input("Do you like the badguys to be aliens or mushrooms?")
      if choice2 == "aliens":
          print("I recommend Halo!")
      elif choice2 == "mushrooms":
          print("I recommend The last of us!")
      else:
          print("That's not a choice")
