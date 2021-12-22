def floodFill(arr,row,col,ans,chkRepeat):
    if row<0 or col<0 or row==len(arr) or col==len(arr[0]) or arr[row][col]==1 or chkRepeat[row][col]==True:
        return
    if row==len(arr)-1 and col==len(arr[0])-1:
        print(ans)
        return
    chkRepeat[row][col]=True
    floodFill(arr,row-1,col,ans+"t",chkRepeat)
    floodFill(arr,row,col-1,ans+"l",chkRepeat)
    floodFill(arr,row+1,col,ans+"b",chkRepeat)
    floodFill(arr,row,col+1,ans+"r",chkRepeat)
    chkRepeat[row][col]=False


visited=[[None]*7 for i in range(6)]
floodFill([[0,1,0,0,0,0,0],
           [0,1,0,1,1,1,0],
           [0,0,0,0,0,0,0],
           [1,0,1,1,0,1,1],
           [1,0,1,1,0,1,1],
           [1,0,0,0,0,0,0]],0,0,"",visited)
floodFill([[1]],0,0,"",visited)
