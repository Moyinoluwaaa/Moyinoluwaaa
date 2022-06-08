import sys
import os


def prime(s):
    # your code goes here
        if s > 1:
            for i in range(2, int(s / 2) + 1):
                if (s % i) == 0:
                    print(s, "is not a prime number")
                    break
            else:
                print(s, "is a prime number")
        else:
            print(s, "is not a prime number")

number = int(input("Enter number: "))


def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error(prime(number)))

    print(solution(sys.argv[1]))
