import sys

# noinspection PyBroadException
try:
    running = True
    while running:
        amount = input("Input amount of diamonds: ")

        def diamond(n):
            if n > 0 and n % 2 == 1:
                diamonds = ""
                stars = 1
                spaces = int((n - 1) / 2)
                for i in range(int(n / 2 + 1)):
                    diamonds += " " * spaces + "*" * stars + "\n"
                    spaces -= 1
                    stars += 2
                stars = n
                spaces = 0
                for i in range(int(n / 2)):
                    spaces += 1
                    stars -= 2
                    diamonds += " " * spaces + "*" * stars + "\n"

            else:
                return None
            print(diamonds)

        diamond(int(amount))
except Exception:
    sys.exit()
