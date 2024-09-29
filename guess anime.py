import random
movies = ["naruto","one piece","attack on titan","bleach","baki","dragon ball z","jujutsu kaisen","demon slayer"]
hints = ["the love story of two ninjas","weird ass people finding sumthing","is the hero, really the hero?","My mom use it on clothes","Sam sulek journey","You will love it if u like balls","A boy eating bhindi without the ladies","Includes a famous pop star"]

def create_question(mov):
    n = len(mov)
    letters = list(mov)
    temp=[]
    for i in range (n):
        if letters[i]==" ":
            temp.append(" ")
        else:
            temp.append("*")
    qn = "".join(str(x) for x in temp)
    return qn

def is_present(letter,picked_mov):
    if letter in picked_mov:
        return True
    return False

def unlock(qn,picked_mov,letter):
    qn = list(qn)
    picked_mov = list(picked_mov)
    temp =[]
    n = len(picked_mov)
    for i in range(n):
        if picked_mov[i]== ' ' or picked_mov[i] == letter:
            temp.append(picked_mov[i])
        else:
            if qn[i]=="*":
                temp.append("*")
            else:
                temp.append(qn[i])
    qn_new = "".join(str(x) for x in temp)
    return qn_new

def play ():
    player1 = input("Player 1! Enter your name :")
    player2 = input("Player 2! Enter your name :")
    # assigning points to both the players
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True
    while(willing):
        if turn%2 == 0 :
            
            print(player1,"Your turn")
            picked_movie = random.choice(movies)
            idex = movies.index(picked_movie)
            print("The Hint for the anime is: ",hints[idex])
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input('Your letter: ')
                if(is_present(letter,picked_movie)):
                    modified_qn = unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d = int(input("Press 1 to guess the anime name or 2 to unlock more character: "))
                    if d==1:
                        ans = input("Enter Your Guess: ")
                        if ans == picked_movie:
                            pp1 = pp1+1
                            print("7 Croooree ! Your answer was right")
                            not_said = False
                            print(player1,"your score is : ",pp1)
                        else:
                            print("the answer is wrong, my advice is to check if its written in lower case")
                else:
                    print("nuh uh, Wrong alphabet")
            c = int(input("press 1 to input or 0 to quit: "))
            if c == 0:
                print(player1,"score :",pp1)
                print(player2,"score :",pp2)
                print("thanks for playing")
                willing = False
            else:
                turn = turn +1
        else :
            print(player2," Your turn")
            picked_movie = random.choice(movies)
            idex = movies.index(picked_movie)
            print("The Hint for the anime is: ",hints[idex])
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input('Your letter: ')
                if(is_present(letter,picked_movie)):
                    modified_qn = unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d = int(input("Press 1 to guess the anime name or 2 to unlock more character: "))
                    if d==1:
                        ans = input("Enter Your Guess: ")
                        if ans == picked_movie:
                            pp2 = pp2+1
                            print("7 Croooree ! Your answer was right")
                            not_said = False
                            print(player2,"your score is : ",pp2)
                        else:
                            print("the answer is wrong, my advice is to check if its written in lower case")
                else:
                    print("nuh uh, Wrong alphabet")
            c = int(input("press 1 to input or 0 to quit: "))
            if c == 0:
                print(player1,"score :",pp1)
                print(player2,"score :",pp2)
                print("thanks for playing")
                willing = False
            else:
                turn = turn +1
play()
