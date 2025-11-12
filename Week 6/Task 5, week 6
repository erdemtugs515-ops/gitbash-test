SEPARATOR = ";"

def readValues(filename) -> str:
    values = ""
    with open(filename, "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            number = lines[i].strip()
            if i < len(lines) - 1:
                values += number + SEPARATOR
            else:
                values += number
    return values

def analyseNumbers(values):
    parts = values.split(SEPARATOR)
    numbers = [int(x) for x in parts]
    total = sum(numbers)
    count = len(numbers)
    greatest = max(numbers)
    average = total / count if count > 0 else 0
    return count, total, greatest, average

def showResults(filename, count, total, greatest, average):
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print("Count;Sum;Greatest;Average")
    print(f"{count};{total};{greatest};{average:.2f}")
    print("\n#### Number analysis - END ####")

def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)
    count, total, greatest, average = analyseNumbers(values)
    showResults(filename, count, total, greatest, average)
    print("Program ending.")

if __name__ == "__main__":
    main()