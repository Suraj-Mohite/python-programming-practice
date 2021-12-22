#input is descending ordered sorted array and target number. find that number in array and return its index

def Binary_Search_Descending(Arr,Target):
    Start=0
    End=len(Arr)-1
    index=-1

    while(Start<=End):
        Mid=Start+((End-Start)//2)
        if(Arr[Mid]==Target):
            index=Mid
            break
        if(Arr[Start]==Target):
            index=Start
            break
        if(Arr[End]==Target):
            index=End
            break
        
        if(Arr[Mid]<Target):
            End=Mid-1
            
        if(Arr[Mid]>Target):
            Start=Mid+1
    return index

print(Binary_Search_Descending([10,9,8,7,6,5,4,3,2,1,0],102))
