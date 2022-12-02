#!/usr/bin/env python3

def buildList():
    # Array of sums of calories per elf
    calories = []

    with open('data.txt', 'r') as f:
        lines = f.readlines()   # List of all lines in input
        counter = 0             # Running sum of calories per elf

        # Iterate over list of inputs
        for line in lines:
            # If the line is blank, add the running count to the array
            if not line.strip():
                calories.append(counter)
                counter = 0
            # If the line has a value, add it to the running count
            else:
                counter += int(line)
    
    return calories


def main():
    calories = buildList()

    # Part 1
    print(max(calories))

    # Part 2
    calories.sort()
    print(calories[-1] + calories[-2] + calories[-3])


if __name__ == "__main__":
    main()