


def cockandballs(cock, balls):
    if (cock == "j") & (balls == "j"):
        print("I will take your shaft and balls")

    elif (cock == "j"):
        print("I will take your cock")

    elif (balls == "j"):
        print("I will take your balls")

    else:
        print(":(")


cock = input("does your cock exist? (n) (j)")
balls = input("do your balls exist? (n) (j)")

cockandballs(cock, balls)