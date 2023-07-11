import sys

def CheckArgs():
    print(f"Filename: {sys.argv[0]}")

    argLen = len(sys.argv)

    if argLen > 1:
        for arg in sys.argv[1:]:
            print(arg)
    else:
        print("No arguments passed.")

def main():

    CheckArgs()


    for i in range(1, 13):
        for j in range(1, 13):
            product = i * j
            print(f"{product}\t", end='')
        print("\n")

main()
