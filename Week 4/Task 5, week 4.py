print("Program starting.\n")
start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

valid = True
if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    valid = False

if not (start < inspection < stop):
    print("Inspection value must be within the range of start and stop.")
    valid = False

print()

if valid:
    print("First loop - inspection with break:")
    line = []
    for i in range(start, stop):
        if i == inspection:
            break
        line.append(str(i))
    print(" ".join(line))
    print("Second loop - inspection with continue:")
    line = []
    for i in range(start, stop):
        if i == inspection:
            continue
        line.append(str(i))
    print(" ".join(line))

print("\nProgram ending.")
