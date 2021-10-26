"""Lets play some tictactoe!"""
import turtle
import random
from grid import grid, box_mark_cross, box_mark_circle


def check_win(check_boxes):
    """Specifies the win condition for the side"""
    # win is possible only if more than two boxes are marked
    while len(check_boxes) > 2:
        # choosing coordinates of three boxes
        for x_coord_1, y_coord_1 in check_boxes:
            coords_1 = []
            for i in check_boxes:
                if i != (x_coord_1, y_coord_1):
                    coords_1.append(i)

            for x_coord_2, y_coord_2 in coords_1:
                coords_2 = []
                for j in coords_1:
                    if j != (x_coord_2, y_coord_2):
                        coords_2.append(j)

                for x_coord_3, y_coord_3 in coords_2:
                    # checking if the points are collinear
                    if (
                        x_coord_1*(y_coord_2 - y_coord_3)
                        + x_coord_2*(y_coord_3 - y_coord_1)
                        + x_coord_3*(y_coord_1 - y_coord_2) == 0
                    ):
                        return True
        # what else do you want me to do?
        return False
    # if you win marking less than three boxes, you're
    # an alien *cough* Mark Zucker..*cough*
    return False


def cont(open_boxes, cross_boxes, circle_boxes):
    """This function returns true if the game is to be continued
     and false if the game is over
     """
    # only need to check if there are 3 or more of the same symbol
    # why is this condition being checked twice? idk
    while len(cross_boxes) > 2 or len(open_boxes) > 2:
        if check_win(circle_boxes) or check_win(cross_boxes):
            return False
        return True
    return True


def try_win(check_boxes, open_boxes):
    """This function returns the box which if marked,
     gives the side a win
     """
    open_box_names = list(open_boxes.keys())
    for x_coord_1, y_coord_1 in check_boxes:
        coords_1 = []
        for i in check_boxes:
            if i != (x_coord_1, y_coord_1):
                coords_1.append(i)

        for x_coord_2, y_coord_2 in coords_1:
            # checking if there is an open box between two marked
            # boxes forming a line
            midpoint = ((x_coord_1 + x_coord_2)/2, (y_coord_1 + y_coord_2)/2)
            values = list(open_boxes.values())

            # no such box, now checking for open boxes beyond two
            # marked boxes forming a line
            if midpoint not in values:
                extpoint = (2*x_coord_1 - x_coord_2, 2*y_coord_1 - y_coord_2)

                # box is present beyond two boxes
                if extpoint in values:
                    index = values.index(extpoint)
                    return open_box_names[index]

            # box is present between two boxes
            else:
                index = values.index(midpoint)
                return open_box_names[index]

    # no boxes which can be marked to win the game
    return False


def best_play(open_boxes, cross_boxes, circle_boxes):
    """This function returns the best move
    that the computer can play
    """
    open_box_names = list(open_boxes.keys())
    while not try_win(circle_boxes, open_boxes):
        if not try_win(cross_boxes, open_boxes):
            if 'mc' in open_boxes:
                first_moves = open_box_names
                for _ in range(10):
                    first_moves.append('mc')
                return random.choice(first_moves)
            if 'mc' not in open_box_names and len(circle_boxes) < 2:
                corners = ['tl', 'tr', 'bl', 'br']
                available_corners = []
                for corner in corners:
                    if corner in open_box_names:
                        available_corners.append(corner)
                return random.choice(available_corners)
            return random.choice(open_box_names)
        return try_win(cross_boxes, open_boxes)
    return try_win(circle_boxes, open_boxes)


def game(start, size=600):
    """Initializes a game of tictactoe in a grid of. The size
    specifies the size of the grid and
    the start parameter defines who has the first move
    """
    # creating a grid
    grid(size)
    mark_size = 30 + 7*size/50
    # the unmarked boxes
    open_boxes = {
        'tl': (-1, 1), 'tc': (0, 1), 'tr': (1, 1),
        'ml': (-1, 0),  'mc': (0, 0), 'mr': (1, 0),
        'bl': (-1, -1), 'bc': (0, -1), 'br': (1, -1)
    }
    # the boxes with circles
    circle_boxes = []
    # the boxes with crosses
    cross_boxes = []
    # the names of the boxes with crosses and boxes with circles
    cross_box_names = circle_box_names = []

    # boxes are not over, so continue the game
    while len(open_boxes) > 0 and cont(open_boxes, cross_boxes, circle_boxes):
        open_box_names = list(open_boxes.keys())

        # the user gets to start first, user is scared of a challenge smh
        if 'user' in start:
            # user input
            cross = input('where do you want to put your mark? '
                          f'The unmarked boxes are {open_box_names}\n').lower()
            # valid input, cross the box
            if cross in open_boxes:
                box_mark_cross(cross, mark_size, size)
                cross_boxes.append(open_boxes.get(cross))
                del open_boxes[cross]
                open_box_names = list(open_boxes.keys())
                cross_box_names.append(cross)

                # computer's turn
                while len(open_boxes) > 0 and cont(open_boxes, cross_boxes, circle_boxes):
                    circle = best_play(open_boxes, cross_boxes, circle_boxes)
                    print(circle)
                    box_mark_circle(circle, mark_size, size)
                    circle_boxes.append(open_boxes.get(circle))
                    del open_boxes[circle]
                    open_box_names = list(open_boxes.keys())
                    circle_box_names.append(circle)
                    break

            # box is already marked
            elif cross in cross_box_names or cross in circle_box_names:
                print('The box has already been marked')
            # or the user provided an invalid input
            else:
                print('Invalid response')

        # the computer gets to start first, the user has some guts
        elif 'computer' in start:
            # plays the best move
            while len(open_boxes) > 0 and cont(open_boxes, cross_boxes, circle_boxes):
                circle = best_play(open_boxes, cross_boxes, circle_boxes)
                print(circle)
                box_mark_circle(circle, mark_size, size)
                circle_boxes.append(open_boxes.get(circle))
                del open_boxes[circle]
                open_box_names = list(open_boxes.keys())
                circle_box_names.append(circle)
                break

            # if boxes are left, asks the user which box to cross
            while len(open_boxes) > 0 and cont(open_boxes, cross_boxes, circle_boxes):
                cross = input('where do you want to put your mark? '
                              f'{open_box_names}\n').lower()
                # valid input, cross the box
                if cross in open_boxes:
                    box_mark_cross(cross, mark_size, size)
                    cross_boxes.append(open_boxes.get(cross))
                    del open_boxes[cross]
                    open_box_names = list(open_boxes.keys())
                    cross_box_names.append(cross)
                    break
                # box is already marked
                if cross in cross_box_names or cross in circle_box_names:
                    print('The box has already been marked')
                # or the user provided an invalid input
                else:
                    print('Invalid response')

    # computer wins, the user is dogshit at tictactoe
    if check_win(circle_boxes):
        print('I win!')
        return False
    # user wins
    if check_win(cross_boxes):
        print('You win!')
        return True
    # match is drawn
    print('It\'s a draw!')


def series_result(win_games, lose_games):
    """Takes the number of games and the won and lost games and
    returns who is the overall winner
    """
    if win_games > lose_games:
        print(f'You have won the series {win_games} - {lose_games} !')
    elif lose_games > win_games:
        # the user is dumber than Trump
        print(f'You have lost the series {win_games} - {lose_games} !')
    else:
        print(f'The series has ended in a draw {win_games} - {lose_games} !')


def series():
    """This function starts a series of tictactoe games"""
    games = int(input('How many games do you want to play?\n'))
    side = input('\nHeads or tails?\n').lower()
    prob_sides = ['heads', 'tails']
    toss = random.choice(prob_sides)
    toss_result = side[0] == toss[0]
    # the user wins the toss, lucky man
    if toss_result:
        print(f'The coin landed on {toss}! You have won the toss')
    # the computer wins the toss
    else:
        print(f'The coin landed on {toss}! Better luck next time')
    # alternates between who gets to start first
    win_games = lose_games = 0
    for chance in range(1, games + 1):
        skip = input('\nShall we continue?\n').lower()
        print('')
        # let the user marvel at his win
        while'y' not in skip:
            skip = input('Are you ready now?\n').lower()
            print('')
        # the user is ready to play
        else:
            print(f'\nGame {chance}\n______\n')
            # toss winner gets to start first for the first game, then
            # it alternates
            if chance % 2 == 1:
                if toss_result:
                    result = game('user')
                    if result:
                        win_games += 1
                    elif result is False:
                        lose_games += 1
                else:
                    result = game('computer')
                    if result:
                        win_games += 1
                    elif result is False:
                        lose_games += 1
            else:
                if not toss_result:
                    result = game('user')
                    if result:
                        win_games += 1
                    elif result is False:
                        lose_games += 1
                        break
                else:
                    result = game('computer')
                    if result:
                        win_games += 1
                    elif result is False:
                        lose_games += 1
    # the series is over
    print('_'*79 + '\n\nPlease close the turtle window when you\'re done\n')
    turtle.mainloop()
    series_result(win_games, lose_games)


series()
