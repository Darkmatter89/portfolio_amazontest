openFile = open('input.txt','r+')
outputFile = open('output.txt','w')

for line in openFile:
    
    a = line.index(':')
    list1 = line[a+2:]
    list1 = list1.replace(" ","")
    list1 = list1.split(",")
    
    list2 = []
    if "max" in line:
        for i in range(0,len(list1)):
            list2.append(int(list1[i]))
        outputFile.write("The max of " + str(list2) + " is "+ str(max(list2)) + ".\n")
        print("The max of " + str(list2) + " is "+ str(max(list2)))
        
    list2 = []
    if "min" in line:
        for i in range(0,len(list1)):
            list2.append(int(list1[i]))
        outputFile.write("The min of " + str(list2) + " is "+ str(min(list2)) + ".\n")
        print("The min of " + str(list2) + " is "+ str(min(list2)))
        
    list2 = []
    if "avg" in line:
        for i in range(0,len(list1)):
            list2.append(int(list1[i]))
        avg = sum(list2) / len(list2)
        outputFile.write("The avg of " + str(list2) + " is "+ str(avg) + ".\n")
        print("The avg of " + str(list2) + " is "+ str(avg))

openFile.close()
outputFile.close()