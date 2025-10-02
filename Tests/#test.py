import sys
import os
answer = input("Did you drink beer? = ").strip().lower()

if answer == "yes":
    print("You can start coding now")
else:
    print("Drink a beer and come back")
    # stop the program
    import sys
    sys.exit(0)




import os
import sys

answer = (input(" Did you drink beer? = "))
if answer.lower() == "yes":
    print("You can start coding now")
else:
     print("Drink a beer and come back")
     sys.exit(0) 
