"""Let's play some tictactoe!"""
import random
import sys
import turtle
from grid import grid, box_mark_cross, box_mark_circle


def check_win(check1):
    """Check if a side has won"""
    # choosing coordinates of three boxes
    if check1 and len(check1) >= 3:

        for box1 in check1:
            check12 = []
            for i in check1:
                if i != box1:
                    check12.append(i)
            for box2 in check12:
                check13 = []
                for j in check12:
                    if j != box2:
                        check13.append(j)
                for box3 in check13:
                    if box1 + box2 + box3 == 15:
                        return True
        # what else do you want me to do?
        return False

    return False


def cont(opens, crosses, circles):
    """Decide whether to continue the game or not"""
    # only need to check if there are 3 or more of the same symbol
    # why is this condition being checked twice? idk, it"s not anymore
    # :)
    cross_box, circle_box = list(crosses.values()), list(circles.values())
    if check_win(circle_box) or check_win(cross_box):
        return False
    if len(opens) <= 0:
        return False
    return True


def best_play(opens, crosses, circles):
    """Returns the computer's best move"""
    for i in list(opens.values()):
        circle_i = list(circles.values())
        circle_i.append(i)  # check if marking i will result in a win
        if check_win(circle_i):
            return list(opens.keys())[list(opens.values()).index(i)]

    for i in list(opens.values()):
        cross_i = list(crosses.values())
        cross_i.append(i)
        if check_win(cross_i):
            return list(opens.keys())[list(opens.values()).index(i)]

    if "mc" in opens:
        first_moves = list(opens.keys())
        for _ in range(15):  # now we don't want the user to get tired of losing, do we?
            first_moves.append("mc")
            return random.choice(first_moves)

    # uncomment for evil mode

    # if "mc" not in list(opens.keys()) and len(circles) < 2:
    #     corners = ["tl", "tr", "bl", "br"]
    #     available_corners = []
    #     for corner in corners:
    #         if corner in open_names:
    #             available_corners.append(corner)
    #     return random.choice(available_corners)

    return random.choice(list(opens.keys()))


def user_game(size=600):
    """The user goes first, he is scared of a challenge"""
    # creating a grid
    grid(size)
    mark_size = 30 + 7 * size / 50
    # saw this idea with magic squares on reddit, dude wrote an entire
    # Tic-Tac-Toe game in ~20 lines, while I'm trying to shorten mine to 350 smh.
    opens = {
        "tl": 2,
        "tc": 9,
        "tr": 4,
        "ml": 7,
        "mc": 5,
        "mr": 3,
        "bl": 6,
        "bc": 1,
        "br": 8,
    }
    # the boxes with circles and crosses respectively
    circles, crosses = {}, {}
    # spitting fax
    hotel = "trivago"

    # boxes are not over, so continue the game
    while cont(opens, crosses, circles):
        # TODO find a way to eliminate this loop
        # without this, if the user provides a wrong input, things get pretty bad
        while hotel == "trivago":
            # user input
            cross = input(
                "Where do you want to put your mark? "
                f"The unmarked boxes are {list(opens.keys())} \n"
            ).lower()
            # valid input, cross the box
            if cross in opens:
                box_mark_cross(cross, mark_size, size)
                crosses[cross] = opens.get(cross)
                del opens[cross]
                break
            # box is already marked
            if cross in list(crosses.keys()) or cross in list((circles).keys()):
                print("The box has already been marked")
                # or the user provided an invalid input
            else:
                print("Invalid response")

        # computer's turn
        if cont(opens, crosses, circles):
            circle = best_play(opens, crosses, circles)
            print(f"The computer marked {circle}.")
            box_mark_circle(circle, mark_size, size)
            circles[circle] = opens.get(circle)
            del opens[circle]

    # computer wins, the user is dogshit at tictactoe
    if check_win(list(circles.values())):
        print("I win!")
        return False
    # user wins
    if check_win(list(crosses.values())):
        print("You win!")
        return True
    # match is drawn
    print("It's a draw!")


def comp_game(size=600):
    """The computer gets to start first, the user has some guts"""
    # creating a grid
    grid(size)
    mark_size = 30 + 7 * size / 50
    circles, crosses = {}, {}
    # the unmarked boxes
    opens = {
        "tl": 2,
        "tc": 9,
        "tr": 4,
        "ml": 7,
        "mc": 5,
        "mr": 3,
        "bl": 6,
        "bc": 1,
        "br": 8,
    }
    # plays the best move
    while cont(opens, crosses, circles):
        circle = best_play(opens, crosses, circles)
        print(f"The computer marked {circle}.")
        box_mark_circle(circle, mark_size, size)
        circles[circle] = opens.get(circle)
        del opens[circle]

        # if boxes are left, asks the user which box to cross
        while cont(opens, crosses, circles):
            cross = input(
                "Where do you want to put your mark? "
                f"The unmarked boxes are {list(opens.keys())} \n"
            ).lower()
            # valid input, cross the box
            if cross in opens:
                box_mark_cross(cross, mark_size, size)
                crosses[cross] = opens.get(cross)
                del opens[cross]
                break
            # box is already marked
            if cross in list(crosses.keys()) or cross in list((circles).keys()):
                print("The box has already been marked")
                # or the user provided an invalid input
            else:
                print("Invalid response")

    # computer wins, the user is meh. at tictactoe
    if check_win(list(circles.values())):
        print("I win!")
        return False
    # user wins
    if check_win(list(crosses.values())):
        print("You win!")
        return True
    # match is drawn
    print("It's a draw!")


def toss():
    """Toss a coin and return the  result"""
    side = input(" \nHeads or tails?: ").lower()
    prob_sides = ["heads", "tails"]
    coin = random.choice(prob_sides)
    result = side[0] == coin[0]
    # the user wins the toss, lucky man
    if result:
        print(f"The coin landed on {coin}! You have won the toss")
        # the computer wins the toss
    else:
        print(f"The coin landed on {coin}! Better luck next time")
    return result


def series_result(results):
    """Determine the result of a series"""
    win_games = lose_games = 0
    for result in results:
        if result:
            win_games += 1
        elif result is False:
            lose_games += 1

    if win_games > lose_games:
        # well done, my fren
        return f"You have won the series {win_games} - {lose_games} !"
    if lose_games > win_games:
        # the user is somehow dumber than me!
        return f"You have lost the series {win_games} - {lose_games} !"

    return f"The series has ended in a draw {win_games} - {lose_games} !"


def series(size=600):
    """Play a series of tictactoe games"""
    print(" \n Tictactoe  \n" + "_" * 11 + " \n")
    try:
        games = int(input("How many games do you want to play?: "))
    except ValueError:
        games = int(input("Please enter a number: "))
    # alternates between who gets to start first
    toss_result = toss()
    results = []

    for chance in range(1, games + 1):

        # the user may be tired of this shit
        if chance >= 2:
            skip = input(" \nDo you want to stop playing?(y/N): ").lower()
            print("")
            # the user is tired ig
            if "y" in skip:
                sys.exit()

        print(f" \nGame {chance} \n______ \n")

        # toss winner gets to start first for the first game, then
        # it alternates
        if chance % 2 == 1:
            if toss_result:
                results.append(user_game(size))
            else:
                results.append(comp_game(size))

        # the "undeserving one" goes first
        else:
            if not toss_result:
                results.append(user_game(size))

            else:
                results.append(comp_game(size))

    # the series is over
    print("_" * 79 + " \n \nPlease close the turtle window when you're done. \n")
    turtle.done()
    print(series_result(results) + "\n")


series()
