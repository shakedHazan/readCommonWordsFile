def main():
    try:
        wordsSorted = readFile()
        count = int(input("Enter the number of words you want to see: "))
        for i in wordsSorted:
            if(count != 0):
                print(i, wordsSorted[i])
                count = count - 1
    except TypeError:
        print("error you need to put a number only")


def readFile():
    wordsCount = {}
    added = False
    try:
        with open("words.txt", "r") as file:
            content = file.read()
            for line in content.split():
                added = False
                for key in wordsCount.keys():
                    if key == line:
                        wordsCount[key] += 1
                        added = True
                if added == False:
                    wordsCount[line] = 1
        return {k : v for k , v in sorted(wordsCount.items(), key = lambda item: item[1], reverse = True)}
    except:
        print("error openning and reading the file")




if __name__ == "__main__":
    main()
