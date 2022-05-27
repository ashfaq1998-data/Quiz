def questions():
    count = 0
    print("Welcome to quiz")
    x = input("There are 6 simple questions which are mcqs. Do you wish to continue(y/n): ")
    if x == 'n':
        exit()
    else:
        print("1. what is the largest river in the world? ")
        print("a. amazon river")
        print("b. nile river")
        print("c. mahaweli river")
        print("d. yamuna river")
        ans1 = input("Your choice is : ")
        if ans1 == 'b':
            count = count + 1
            print("Correct answer")

        else:
            print("Incorrect answer")
            print("Nile river is right answer")

        print("2. what is brain of the computer? ")
        print("a. monitor")
        print("b. key board")
        print("c. CPU")
        print("d. UPS")
        ans1 = input("Your choice is : ")
        if ans1 == 'c':
            count = count + 1
            print("Correct answer")
        else:
            print("Incorrect answer")
            print("CPU is correct answer")

        print("3. If the length of square is 2m, find the area? ")
        print("a. 4m")
        print("b. 8m")
        print("c. 12m")
        print("d. 80m")
        ans1 = input("Your choice is : ")
        if ans1 == 'a':
            count = count + 1
            print("Correct answer")
        else:
            print("Incorrect answer")
            print("4m is correct answer")

        print("4. Which of the followings are vowel letters? ")
        print("a. auiow")
        print("b. qyuiw")
        print("c. ioefsoh")
        print("d. aeiou")
        ans1 = input("Your choice is : ")
        if ans1 == 'd':
            count = count + 1
            print("Correct answer")
        else:
            print("Incorrect answer")
            print("aeiou is correct answer")

        print("5. What is oldest university in sri lanka? ")
        print("a. University of Colombo")
        print("b. University of Moratuwa")
        print("c. University of Jaffna")
        print("d. University of Ruhunu")
        ans1 = input("Your choice is : ")
        if ans1 == 'a':
            count = count + 1
            print("Correct answer")
        else:
            print("Incorrect answer")
            print("University of Colombo is correct answer")

        print("6. Elephant orphanage in sri lanka? ")
        print("a. nuwera eliya")
        print("b. jaffna")
        print("c. colombo")
        print("d. pinnewala")
        ans1 = input("Your choice is : ")
        if ans1 == 'd':
            count = count + 1
            print("Correct answer")
        else:
            print("Incorrect answer")
            print("pinnewala is correct answer")

        print("Your total score is ",count)


while True:
    questions()
    res = input("Do you wish to redo ?(y/n)")
    if res == 'n':
        break




