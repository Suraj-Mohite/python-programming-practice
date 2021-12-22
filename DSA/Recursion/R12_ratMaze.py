"""
def ratMaze(sr,sc,er,ec):
    if sr==er and sc==ec:
        return [""]
    
    HorPath=[]
    if sc<ec:
        HorPath=ratMaze(sr,sc+1,er,ec)
    VerPath=[]
    if sr<er:
        VerPath=ratMaze(sr+1,sc,er,ec)
    
    path=[]
    for i in HorPath:
        path.append("h"+i)
    for i in VerPath:
        path.append("v"+i)
    
    return path
"""

# def ratMazeX(sr,sc,er,ec):
#     if sr==er and sc==ec:
#         return [""]
#     path=[]
#     HorPath=[]
#     if sc<ec:
#         HorPath=ratMazeX(sr,sc+1,er,ec)
#         for i in HorPath:
#             path.append("h"+i)
#     DiaPath=[]
#     if sc<ec and sr<er:
#         DiaPath=ratMazeX(sr+1,sc+1,er,ec)
#         for i in DiaPath:
#             path.append("d"+i)

#     VerPath=[]
#     if sr<er:
#         VerPath=ratMazeX(sr+1,sc,er,ec)
#         for i in VerPath:
#             path.append("v"+i)
    
#     return path

def ratMazeXX(sr,sc,er,ec):
    if sr==er and sc==ec:
        return [""]
    if sr>er and sc>ec:
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

def ratMazeJump(sr,sc,er,ec):
    if sr==er and sc==ec:
        return [""]
    if sr>er and sc>ec:
        return []
    
    HorPath=[]
    path=[]
    if sc<ec:
        for i in range(1,ec+1):
            HorPath=ratMazeJump(sr,sc+i,er,ec)
            for j in HorPath:
                path.append("h"+str(i)+j)

    DiaPath=[]
    if sc<ec and sr<er:
        for i in range(1,ec+1):
            DiaPath=ratMazeJump(sr+i,sc+i,er,ec)
            for j in DiaPath:
                path.append("d"+str(i)+j)
    VerPath=[]
    if sr<er:
        for i in range(1,er+1):
            VerPath=ratMazeJump(sr+i,sc,er,ec)
            for j in VerPath:
                path.append("v"+str(i)+j)
    
    return path


print(ratMazeJump(0,0,3,3))
# print(ratMazeXX(0,0,3,2))

    