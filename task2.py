def my_task2():
    filename = 'data.txt'
    fileObj = open(filename, "r")
    words = fileObj.read().splitlines()
    fileObj.close
    
    # a = sorted(words, key=lambda x: x, reverse=False)
    # return a
    n = len(words)
    first = []
    temps = []
    third = []
    # for i in range(n):
    #     for j in range(n-1):
    #         if int(words[j]) > int(words[j+1]):
    #             words[j], words[j+1] = words[j+1], words[j]

    for i in range(n):
        for j in range(n-1):
            temp = 2020 - int(words[j]) - int(words[j+1])
            temps.append(temp)
            if int(temps[i])>0:    
                first = temps[i]

    second = 2020 - int(first)
    return(third,second)

def main():
    print(my_task2())

if __name__ =="__main__":
    main()