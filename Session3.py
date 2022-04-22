def main():
    answer = testfunction(9)
    print(answer)
    if (answer > 27):
        print("YAY!")

def testfunction(x):
    return (x**3 + 8)

main()