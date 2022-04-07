def pagerank():
    print('Enter the Matrix')
    array_input=[]
    for x in range(3):
        array_input.append([float(y) for y in input().split()])
    print(array_input)
    
    finalmat=[1,1,1]
    itr = int(input('Enter the number of iterations'))
    
    for loop in range(itr):
        print('Iteration:',loop+1)
        cnt=0
        for row in range(len(array_input)):
            sum=0
            for col in range(len(array_input[row])):
                if(array_input[col][row]==1):
                    for i in range(3):
                        if(array_input[col][i]==1):
                            cnt=cnt+1
                    sum+=finalmat[col]/cnt
                cnt=0
            finalmat[row]=0.5+(0.5*sum)
            print(finalmat[row],'')
pagerank()
