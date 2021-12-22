"""def returnSteps(no,cnt):
    if no==0:
        return [""],cnt
    if no<0:
        return [],cnt
    path1=returnSteps(no-1,cnt)
    
    path2=returnSteps(no-2,cnt)

    path3=returnSteps(no-3,cnt)

    path=[]

    for i in path1[0]:
        path.append("1"+i)
        cnt+=1
    for i in path2[0]:
        path.append("2"+i)
        cnt+=1
    for i in path3[0]:
        path.append("3"+i)
        cnt+=1
    return path,cnt"""

def returnSteps(no,cnt):
    if no==0:
        return [""],cnt
    if no<0:
        return [],cnt
    path=[]
    path1=returnSteps(no-1,cnt)
    for i in path1[0]:
        path.append("1"+i)
        cnt+=1
    path2=returnSteps(no-2,cnt)
    for i in path2[0]:
        path.append("2"+i)
        cnt+=1
    path3=returnSteps(no-3,cnt)
    for i in path3[0]:
        path.append("3"+i)
        cnt+=1
    

    return path,cnt


print(returnSteps(4,0))
