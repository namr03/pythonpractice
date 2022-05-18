combinations = {
    1 : 3,
    2 : 1,
    3 : 2
}
while True:
    game = input("Start or stop game?: ").lower()
    if game == "stop":
        break
    elif game == "start":
        points1 = 0
        points2 = 0
        while True:
            p1 = int(input("PLAYER 1 Choose rock , paper or scissors " + "\n" + "1 - Rock, 2 - Paper, 3 - Scissors:  "))
            while p1 not in combinations:
                print("wrong input")
                p1 = int(
                    input("PLAYER 1 Choose rock , paper or scissors " + "\n" + "1 - Rock, 2 - Paper, 3 - Scissors:  "))
            p2 = int(input("PLAYER 2 Choose rock , paper or scissors " + "\n" + "1 - Rock, 2 - Paper, 3 - Scissors:  "))
            while p2 not in combinations:
                print("wrong input")
                p2 = int(
                    input("PLAYER 2 Choose rock , paper or scissors " + "\n" + "1 - Rock, 2 - Paper, 3 - Scissors:  "))
            if combinations[p1] == p2:
                print("p1 won")
                points1 += 1

            elif combinations[p2] == p1:
                print("p2 won")
                points2 += 1
            elif p2 == p1:
                print("Draw")
            if points1 == 10:
                print("Player 1 won!")
                quit()
            elif points2 == 10:
                print("Player 2 won!")
                quit()
    else:
        continue
