def find_max_sum(numbers):
    largest = 0
    second_largest = 0
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or second_largest < num:
            second_largest = num
    return largest + second_largest


if __name__ == "__main__":
    print(find_max_sum([5, 9, 7, 1]))

