"""
Problem A. Magic Trick
https://code.google.com/codejam/contest/2974486/dashboard#s=p0

Recently you went to a magic show. You were very impressed by one of the tricks, so you decided to try to figure out the secret behind it!

The magician starts by arranging 16 cards in a square grid: 4 rows of cards, with 4 cards in each row. Each card has a different number from 1 to 16 written on the side that is showing. Next, the magician asks a volunteer to choose a card, and to tell him which row that card is in.

Finally, the magician arranges the 16 cards in a square grid again, possibly in a different order. Once again, he asks the volunteer which row her card is in. With only the answers to these two questions, the magician then correctly determines which card the volunteer chose. Amazing, right?

You decide to write a program to help you understand the magician's technique. The program will be given the two arrangements of the cards, and the volunteer's answers to the two questions: the row number of the selected card in the first arrangement, and the row number of the selected card in the second arrangement. The rows are numbered 1 to 4 from top to bottom.

Your program should determine which card the volunteer chose; or if there is more than one card the volunteer might have chosen (the magician did a bad job); or if there's no card consistent with the volunteer's answers (the volunteer cheated).
"""


def solve(a, b):
    intersection = set(a) & set(b)
    N = len(intersection)

    if N == 0:
        return "Volunteer cheated!"
    elif N > 1:
        return "Bad magician!"
    else:
        return intersection.pop()


if __name__ == "__main__":
    testcases = int(input())

    for caseNr in range(1, testcases+1):
        a = int(input()) - 1
        grid = []

        for row in range(1, 5):
            grid.append(input().split(" "))

        b = int(input()) - 1
        grid2 = []

        for row in range(1, 5):
            grid2.append(input().split(" "))

        print("Case #{}: {}".format(caseNr, solve(grid[a], grid2[b])))
