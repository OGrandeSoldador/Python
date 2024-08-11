def sortedlist(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            i += 1
        elif numbers[i] == numbers[i + 1]:
            i += 1
        else:
            numbers[i],numbers[i + 1] = numbers[i + 1],numbers[i]
            return sortedlist(numbers)
    return numbers


def main():
    numbers = [5,4,3,2,1]

    print(sortedlist(numbers))


if __name__ == "__main__":
    main()
