# def chessBoard(cell1,cell2):
#     c1=ord(cell1[0])
#     c2=ord(cell2[0])
#     c1_color=0
#     c2_color=0
#     if((c1%2==0 and int(cell1[1])%2==0)or(c1%2!=0 and int(cell1[1])%2!=0)):
#         c1_color=1
#     if((c2%2==0 and int(cell2[1])%2==0)or(c2%2!=0 and int(cell2[1])%2!=0)):
#         c2_color=1
    
#     if(c1_color==c2_color):
#         return True
#     return False

def chessBoard(cell1,cell2):
    c1=ord(cell1[0])
    c2=ord(cell2[0])
    
    c1_color=0
    c2_color=0
    if((c1%2==0 and int(cell1[1])%2==0)or(c1%2!=0 and int(cell1[1])%2!=0)) and ((c2%2==0 and int(cell2[1])%2==0)or(c2%2!=0 and int(cell2[1])%2!=0)):
        return True
    return False

print(chessBoard("e5","h5"))
# print(chessBoard("A0","H3"))