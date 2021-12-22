#we dont know whether array is ascending or descending retun index of target number if it is present in given sorted array

def Not_Known(Arr,Target):
    Start=0
    End=len(Arr)-1
    index=-1

    if(Arr[0]<Arr[len(Arr)-1]):
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
                Start=Mid+1
            if(Arr[Mid]>Target):
                End=Mid-1
        return index
        
    else:
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

print(Not_Known([5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],5))
print(Not_Known([10,9,8,7,6,5,4,3,2,1,0],6))
