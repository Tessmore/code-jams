"""

Counting sheep: https://code.google.com/codejam/contest/6254486/dashboard#s=p0


Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. First, she picks a number N. Then she starts naming N, 2 × N, 3 × N, and so on. Whenever she names a number, she thinks about all of the digits in that number. She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once so far as part of any number she has named. Once she has seen each of the ten digits at least once, she will fall asleep.

Bleatrix must start with N and must always name (i + 1) × N directly after i × N. For example, suppose that Bleatrix picks N = 1692. She would count as follows:

 N = 1692. Now she has seen the digits 1, 2, 6, and 9.
2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
3N = 5076. Now she has seen all ten digits, and falls asleep.

What is the last number that she will name before falling asleep? If she will count forever, print INSOMNIA instead.

"""

sheep = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

t = int(input())


for i in range(1, t+1):
    N = int(input())

    if N == 0:
        print("Case #{}: {}".format(i, "INSOMNIA"))
        continue

    seen = set()

    for x in range(1, 1000000):
        seen |= set(str(x * N))

        if not (sheep - seen):
            print("Case #{}: {}".format(i, x*N))
            break
    else:
        print("Case #{}: {}".format(i, "INSOMNIA"))
