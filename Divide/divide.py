

def replace_string(text):
    newText1 = text.replace("\"", "")
    newText2 = newText1.replace(" ", ",", 1)
    newText3 = newText2.replace(" - ", "-")
    newText4 = newText3.replace(" – ", "-")
    return newText4


with open("input.csv") as inFile:
    for line in inFile:
        line = line.strip()
        print(replace_string(line))
        with open("output.csv", 'a') as outputFile:
            outputFile.write(replace_string(line))
            outputFile.write("\n")
