def iterative_levenshtein (s, t):
    rows= len (s) +1
    cols= len (t) +1
    dist = [[0 for x in range (cols)] for x in range (rows) ]
    
    cnt=0
    for i in range (1, rows) : 
        cnt=cnt+1
        dist[i][0] = cnt
        
    cnt=0
    for i in range (1, cols):
        cnt=cnt+1 
        dist [0] [i] = cnt
    
    for row in range (1, rows):
        for col in range (1, cols): 
            if s[row-1] == t[col-1]:
                dist [row] [col] = dist[row-1] [col-1] 
            else:
                dist [row] [col] = min (dist [row-1] [col] + 1, dist [row] [col-1]+ 1, dist [row-1] [col-1]+1)
                
    for r in range(rows):
        print(dist[r])
        
    return dist[row][col]

s1=input("Enter String 1:")
s2=input("Enter String 2:")
print("Edit distance between",s1,"and",s2,"is",iterative_levenshtein (s1,s2))
