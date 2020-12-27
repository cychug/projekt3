

def replaceString(text):
    newText1 = text.replace("\"", "")
    newText2 = newText1.replace(" ", ",", 1)
    newText3 = newText2.replace(" - ", "-")
    newText4 = newText3.replace(" – ", "-")
    return newText4


with open("/Users/kwisniewski/Desktop/projekt3/Divide/input.csv") as inFile:
    for line in inFile:
        line = line.strip()
        print(replaceString(line))
        with open("/Users/kwisniewski/Desktop/projekt3/Divide/output.csv", 'a') as outputFile:
            outputFile.write(replaceString(line))
            outputFile.write("\n")

