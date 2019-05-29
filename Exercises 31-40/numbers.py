def numbers_loop(i, x):
    numbers = []
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 2
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)