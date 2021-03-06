def my_task1():
    filename = 'data.txt'
    fileObj = open(filename, "r")
    words = fileObj.read().splitlines()
    fileObj.close

    n = len(words)

    temps = []
    first = []
    second = []
    second2 = []

    for i in range(n):
        temp = 2020 - int(words[i])
        temps.append(temp)
        for j in range(len(temps)):
            if int(temps[i])==int(words[j]):    
                x = temps[i]
                first.append(x)
    
    temp2 = 2020 - first[0]
    multiply = temp2 * first[0];
    print(temp2, first[0], multiply)
    
    # second.append(temp2)
    
    # for k in range(n):
    #     for l in range(len(second)-1):
    #         print(second)
    #          if int(second[k])==int(words[j]):
    #            y = second[k]
    #            second2.append(y)

    # print(y)            

    # print(second2)
    # for temps in words:
    #     i = 0
    #     i = i + 1
    #     print(i)
    #     print(temps in words)

    # for in range(n):

    # for i in range(n):
    #     for j in range(n-1):
    #         if int(words[j]) > int(words[j+1]):
    #             words[j], words[j+1] = words[j+1], words[j]

    # for i in range(n):
    #     for j in range(n-1):
    #         if int(words[j]) + int(words[j+1]) == 2020:
    #             print("ada")

if __name__ == "__main__":
    my_task1()

