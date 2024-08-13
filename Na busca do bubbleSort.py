def sortedlist(numbers):
    b = 1
    j = -1
    while b != 0:
        j += 1
        b = 0
        for i in range(0,(len(numbers) - 1) - j,1):
            if numbers[i] > numbers[i + 1]:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
                b = 1
    return numbers


def main():
    numbers = [5,4,5,6,1,2]

    print(sortedlist(numbers))


if __name__ == "__main__":
    main()
