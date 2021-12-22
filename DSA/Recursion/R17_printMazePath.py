#everywhere sr and sc always starts from 1


def printMazePathHR(sr,sc,er,ec,ans):
    if sr==er and sc==ec:
        print(ans,end=" ")
        return
    if sc<ec:
        printMazePathHR(sr,sc+1,er,ec,ans+"h")
    if sr<er:
        printMazePathHR(sr+1,sc,er,ec,ans+"r")

def printMazePathHDR(sr,sc,er,ec,ans):
    if sr==er and sc==ec:
        print(ans,end=" ")
        return
    if sc<ec:
        printMazePathHDR(sr,sc+1,er,ec,ans+"h")
    if sc<ec and sr<er:
        printMazePathHDR(sr+1,sc+1,er,ec,ans+"d")
    if sr<er:
        printMazePathHDR(sr+1,sc,er,ec,ans+"r")

def printMazePathX(sr,sc,er,ec,ans):
    if sr==er and sc==ec:
        print(ans,end=" ")
        return
    if sr>er or sc>ec:
        return
    if sc<ec:
        printMazePathX(sr,sc+1,er,ec,ans+"h"+"1") 
        printMazePathX(sr,sc+2,er,ec,ans+"h"+"2") 
    if sr<er:
        printMazePathX(sr+1,sc,er,ec,ans+"r"+"1")
        printMazePathX(sr+2,sc,er,ec,ans+"r"+"2")

def printMazePathXX(sr,sc,er,ec,ans):
    if sr==er and sc==ec:
        print(ans,end=" ")
        return
    if sr>er or sc>ec:
        return
    if sc<ec:
        printMazePathXX(sr,sc+1,er,ec,ans+"h"+"1") 
        printMazePathXX(sr,sc+2,er,ec,ans+"h"+"2") 
    if sc<ec and sr<er:
        printMazePathXX(sr+1,sc+1,er,ec,ans+"d"+"1") 
        printMazePathXX(sr+2,sc+2,er,ec,ans+"d"+"2") 
    if sr<er:
        printMazePathXX(sr+1,sc,er,ec,ans+"r"+"1")
        printMazePathXX(sr+2,sc,er,ec,ans+"r"+"2")

def printMazePathJump(sr,sc,er,ec,ans):
    if sr==er and sc==ec:
        print(ans,end=" ")
        return
    # if sr>er or sc>ec:
    #     return
    if sc<ec:
        for i in range(1,(ec-sc)+1):
            printMazePathJump(sr,sc+i,er,ec,ans+"h"+str(i)) 
     
    if sr<er:
        for i in range(1,(er-sr)+1): 
            printMazePathJump(sr+i,sc,er,ec,ans+"r"+str(i))
    if sc<ec and sr<er:
        for i in range(1,(ec-sc)+1):
            printMazePathJump(sr+i,sc+i,er,ec,ans+"d"+str(i))

def printMazePathJumpx(sr,sc,er,ec,ans): #everywhere sr and sc always starts from 1
    if sr==er and sc==ec:
        print(ans,end=" ")
        return
    # if sr>er or sc>ec:
    #     return
    for i in range(1,(ec-sc)+1):
        printMazePathJumpx(sr,sc+i,er,ec,ans+"h"+str(i)) 
     
    for i in range(1,(er-sr)+1): 
        printMazePathJumpx(sr+i,sc,er,ec,ans+"r"+str(i))
    k=1
    while k<=ec-sc and k<=er-sr:
        printMazePathJumpx(sr+k,sc+k,er,ec,ans+"d"+str(k))
        k+=1

def ratMazeXX(sr,sc,er,ec):
    if sr==er and sc==ec:
        return [""]
    if sr>er or sc>ec:
        return []
    
    HorPath=[]
    path=[]
    if sc<ec:
        for i in range(1,3):
            HorPath=ratMazeXX(sr,sc+i,er,ec)
            for j in HorPath:
                path.append("h"+str(i)+j)

    DiaPath=[]
    if sc<ec and sr<er:
        for i in range(1,3):
            DiaPath=ratMazeXX(sr+i,sc+i,er,ec)
            for j in DiaPath:
                path.append("d"+str(i)+j)

    VerPath=[]
    if sr<er:
        for i in range(1,3):
            VerPath=ratMazeXX(sr+i,sc,er,ec)
            for j in VerPath:
                path.append("v"+str(i)+j)
    
    return path

printMazePathJump(1,1,5,2,"")
print()
printMazePathJumpx(1,1,5,2,"")
# print("--"*70)
# print(ratMazeXX(1,1,5,2))