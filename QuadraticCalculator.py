import math



print("This only works if you have a proper quadratic formula,")
print("so make sure you have one")
print("also note that if the program returns an error, there is no solution")

print(" ")

print("what's a?")
aVar = input()
print("what's b?")
bVar = input()
print("what's c?")
cVar = input()
# these output strings by default so Im turning them to floating point numbers
aVarNum = float(aVar)
bVarNum = float(bVar)
cVarNum = float(cVar)


# this is the b^2 part
bSquared = bVarNum ** 2.0

# this is the 4ac part
underSquare = bSquared - (4.0 * aVarNum * cVarNum)

# squaring but only returning positive
squaredPos = (math.sqrt(underSquare))

# getting the negative square as well
squaredNeg = squaredPos * -1.0

# getting negative b
bVarNeg = bVarNum * -1.0

# adding negative b
overPos = bVarNeg + squaredPos
overNeg = bVarNeg + squaredNeg

# dividing over by 2a
answerPos = overPos / (2 * aVarNum)
answerNeg = overNeg / (2 * aVarNum)
answerNegR = round(answerNeg , 2)
answerPosR = round(answerPos , 2)
print(f"your answers are {answerPosR}, and {answerNegR}.")
