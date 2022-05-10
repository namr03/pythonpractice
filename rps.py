while True:
    game = input("Start or stop game?: ").lower()
    if game == "stop":
        break
    elif game == "start":
        wynik1 = 0
        wynik2 = 0
        while True:
            print("-----------------------------------\n" * 10)
            p1 = int(input("PLAYER 1 Choose rock , paper or scissors " + "\n" + "1 - Rock, 2 - Paper, 3 - Scissors:  "))
            if p1 > 3 or p1 < 1:
                print("Incorrect answer PLAYER 1")
                continue
            print("-----------------------------------\n" * 10)
            p2 = int(input("PLAYER 2 Choose rock , paper or scissors " + "\n" + "1 - Rock, 2 - Paper, 3 - Scissors:  "))
            if p2 > 3 or p2 < 1:
                print("Incorrect answer PLAYER 2")
                continue
            else:
                if p1 == 1 and p2 == 1:
                    print("It's a draw" + "\n")
                    continue
                if p1 == 2 and p2 == 2:
                    print("It's a draw" + "\n")
                    continue
                if p1 == 3 and p2 == 3:
                    print("It's a draw" + "\n")
                    continue
                elif p1 == 1 and p2 == 2:
                    print("Player 2 wins a round" + "\n")
                    wynik2 += 1
                    if wynik1 == 5:
                        print("Player 1 wins by ", int(wynik1-wynik2), "Points")
                        quit()
                    elif wynik2 == 5:
                        print("Player 2 wins by ", int(wynik2-wynik1), "Points")
                        quit()
                elif p1 == 1 and p2 == 3:
                    print("Player 1 wins a round" + "\n")
                    wynik1 += 1
                    if wynik1 == 5:
                        print("Player 1 wins by ", int(wynik1-wynik2), "Points")
                        quit()
                    elif wynik2 == 5:
                        print("Player 2 wins by ", int(wynik2-wynik1), "Points")
                        quit()
                elif p1 == 2 and p2 == 1:
                    print("Player 1 wins a round" + "\n")
                    wynik1 += 1
                    if wynik1 == 5:
                        print("Player 1 wins by ", int(wynik1-wynik2), "Points")
                        quit()
                    elif wynik2 == 5:
                        print("Player 2 wins by ", int(wynik2-wynik1), "Points")
                        quit()
                elif p1 == 2 and p2 == 3:
                    print("Player 2 wins a round" + "\n")
                    wynik2 += 1
                    if wynik1 == 5:
                        print("Player 1 wins by ", int(wynik1-wynik2), "Points")
                        quit()
                    elif wynik2 == 5:
                        print("Player 2 wins by ", int(wynik2-wynik1), "Points")
                        quit()

    else:
        continue
