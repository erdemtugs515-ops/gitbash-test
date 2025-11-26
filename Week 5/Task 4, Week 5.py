def askDimension(PPrompt: str) -> float:
    Feed = float(input(f"Insert {PPrompt}: "))
    return Feed

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    return PWidth * PHeight

Width = askDimension("width")
Height = askDimension("height")

Area = calcRectangleArea(Width, Height)

print("")
print(f"Area is {Area}²")
print("end")
