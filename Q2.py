ui1 = ['1 alex','1 Alex','2 sam','1 alix','1 Alix','2 caM']

#ui2 = ['3 jun','3 Jin','1 Li','2 Kitty','2 Josh','3 Bob','1 Dave','2 Jose','1 David','3 Rob','3 Anne','3 Ann','2 Kevin','2 Lara','1 ALI','3 Xin']

# INPUT
# alex Alex alix Alix
# sam caM

# INPUT
# li dave david ali
# kitty josh jose kevin lara
# jun jin bob rob anne ann xin

def main():
    nameList = []
    courseList = []
    for i in range(len(ui1)):
        # names = 1 alex
        names = ui1[i].split(' ')
        if int(names[0]) not in courseList:
            courseList.append(int(names[0]))
        #print(names)
        #nameList[i][0] = names[0]
        #names[1]=names[1].lower()
        nameList.append(names)

    print(nameList)
    print(courseList)
    data = []
    for j in courseList:
        studentNames = []
        for i in range(len(nameList)):
            # print(nameList[i], "*", int(nameList[i][0]))
            if j == int(nameList[i][0]):
                studentNames.append(nameList[i][1].lower())
        data.append(studentNames)

    #print("your 2D array:")
    #for row in data:
        #print(row)
    print(data[0])
    similarNames(data[0])

def similarNames(classNumber):
    #'alex', 'Alex', 'alix', 'Alix'
    # 4 times
    newNames = []
    similarIndices = []
    for i in range(len(classNumber)):
        for j in range(len(classNumber)):
            if j > i:
                print("compare: ", classNumber[i], " vs. ", classNumber[j])
                if len(classNumber[i]) == len(classNumber[j]):
                    counter = 0
                    for k in range(len(classNumber[i])):
                        if classNumber[i][k] != classNumber[j][k]:
                            # print(counter,"*", classNumber[j][k])
                            counter += 1

                    if counter > 1:
                        print(classNumber[j], "is NOT SIMILAR")

                    else:
                        print(classNumber[j], "is similar, we need to add the index of this name to the remove list **",j)
                        if j not in similarIndices:
                            similarIndices.append(j)

    print("similar indices: ", similarIndices)
    namesToKeep = []
    for i in range(len(classNumber)):
        if i not in similarIndices:
            namesToKeep.append(classNumber[i])

    print(namesToKeep)


main()
