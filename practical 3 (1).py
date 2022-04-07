plays={"Anthony and Cleopatra":"Anthony is there, Brutus is Caeser is with Cleopatra mercy worser.",
       "Julius Ceaser":"Anthony is there, Brutus is Caeser is but Calpurnia is.",
       "The Tempest":"mercy worser","Hamlet":"Caeser and Brutus are present with mercy and worser",
       "Othello":"Caeser is present with mercy and worser","Macbeth":"Anthony is there, Caeser mercy."}
words=["Anthony","Brutus","Caeser","Calpurnia","Cleopatra","mercy","worser"]
vector_matrix=[[0 for i in range (len (plays))] for j in range (len (words))]
text_list=list ((plays.values()))

for i in range (len (words)) :
    for j in range (len (text_list)):
        if words [i] in text_list[j]:
            vector_matrix[i][j]=1
        else:
            vector_matrix [i][j] =0

for i in vector_matrix:
    print (i)

#result=[]

string_list=[]
for vector in vector_matrix:
    mystring=""
    for digit in vector:
        mystring += str(digit)
    string_list.append(int (mystring))
print (string_list)

print("The output is ", bin(string_list [0] & string_list [1] & string_list [2] & string_list [3]).replace("0b",""))

#print ("The output is ",bin (string_list[0] & string_list [1] & (string_list[2])).replace ("Ob",""))
