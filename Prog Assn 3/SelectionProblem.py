import sys

#Merge Sort Algorith from Programming Assignment 
def merge_sort(arr,low,high):
    if low!=high:
        mid=(low+high)/2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr,low,mid,high)
    return arr    
        
def merge(arr,low,mid,high):
    temp= [None]*len(arr)
    i=low
    j=mid+1
    k=low
    while i<=mid and j<=high:
        if arr[i][1]<=arr[j][1]:
            temp[k]=arr[i]
            k=k+1
            i=i+1
        else:
            temp[k]=arr[j]
            k=k+1
            j=j+1
    while i<=mid:
        temp[k]=arr[i]
        k=k+1
        i=i+1
    while j<=high:
        temp[k]=arr[j]
        k=k+1
        j=j+1
    for i in range(low,high+1):   
        arr[i]=temp[i]
 
#Job Selection Function
def selection_problem(start_state):
#   Data Structure for Dynamic Programming
    dynamic_max_weight=[-1]*len(start_state)
    dynamic_max_weight[0]=start_state[0][2]
    for i in range(1,len(start_state)):
        low=0
        high=i-1
        new_weight=-1
#       Binary Search for the first previous element that satisfies constarint  
        while(low<=high):
            mid=(low+high)/2
            if(start_state[mid][1]<=start_state[i][0]):
                if(start_state[mid+1][1]<=start_state[i][0]):
                    low=mid+1
                else:
                    new_weight=start_state[i][2]+dynamic_max_weight[mid]
                    break    
            else:        
                high=mid-1
            
        if(new_weight!=-1):
            dynamic_max_weight[i]=max(new_weight,dynamic_max_weight[i-1])
        else:
            dynamic_max_weight[i]=max(start_state[i][2],dynamic_max_weight[i-1])    
    return dynamic_max_weight[len(start_state)-1]
    
# filename="input1.txt"
start_state=[]
with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [[int(i) for i in line.split()]]
             
merge_sort(start_state,0,len(start_state)-1)
print(selection_problem(start_state))