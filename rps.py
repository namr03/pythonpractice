while True:
    game = input("Start or stop game?: ").lower()
    if game == "quit":
        break
    elif game == "start":
        wynik1 = 0
        wynik2 = 0
        while True:
            p1 = int(input("Choose rock , paper or scissors " + "\n" + "1 - Rock, 2 - Paper, 3 - Scissors:  "))
            print("-----------------------------------\n"*20)
            p2 = int(input("Choose rock , paper or scissors " + "\n" + "1 - Rock, 2 - Paper, 3 - Scissors:  "))
            if p1 == 1 and p2 == 1:
                print("It's a draw")
                continue
            if p1 == 2 and p2 == 2:
                print("It's a draw")
                continue
            if p1 == 3 and p2 == 3:
                print("It's a draw")
                continue
            elif p1 == 1 and p2 == 2:
                print("Player 2 wins a round")
                wynik2 += 1
                if wynik1 == 5:
                    print("Player 1 wins by " ,int(wynik1-wynik2) ,"Points")
                    quit()
                elif wynik2 == 5:
                    print("Player 2 wins by " ,int(wynik2-wynik1) ,"Points")
                    quit()
            elif p1 == 1 and p2 == 3:
                print("Player 1 wins a round")
                wynik1 += 1
                if wynik1 == 5:
                    print("Player 1 wins by ", int(wynik1-wynik2), "Points")
                    quit()
                elif wynik2 == 5:
                    print("Player 2 wins by ", int(wynik2-wynik1), "Points")
                    quit()
            elif p1 == 2 and p2 == 1:
                print("Player 1 wins a round")
                wynik1 += 1
                if wynik1 == 5:
                    print("Player 1 wins by ", int(wynik1-wynik2),"Points")
                    quit()
                elif wynik2 == 5:
                    print("Player 2 wins by ", int(wynik2-wynik1), "Points")
                    quit()
            elif p1 == 2 and p2 == 3:
                print("Player 2 wins a round")
                wynik2 += 1
                if wynik1 == 5:
                    print("Player 1 wins by ", int(wynik1-wynik2), "Points")
                    quit()
                elif wynik2 == 5:
                    print("Player 2 wins by ", int(wynik2-wynik1), "Points")
                    quit()
    else:
        continue
