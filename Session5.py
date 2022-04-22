import math

def main():
    x = 0.0
    a = (2 * math.pi)/1000
    xlist = []
    ylist = []

    while x < (2 * math.pi):
        print("x value: " + str(x) + "\tsin x value: " + str(math.sin(x)))
        x += a

main()