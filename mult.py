import sys

def CheckArgs():
    print(f"Filename: {sys.argv[0]}")

    argLen = len(sys.argv)

    if argLen > 1:
        for arg in sys.argv[1:]:
            print(arg)
    else:
        print("No arguments passed.")


# Print a multiplication table with values from 1 to 'value'
def PrintTable(value):
    maxValue = value + 1
    for i in range(1, maxValue):
        for j in range(1, maxValue):
            product = i * j
            print(f"{product}\t", end='')
        print("\n")


def main():

    CheckArgs()

    PrintTable(12)

main()
