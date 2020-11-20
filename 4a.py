# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:08:21 2020

@author: rajee
"""

a=[8,9,7,6]
def partition(a,first,last):
    if first>=last:
        return 
    if a[first]>a[first+1]:
        a[first],a[first+1]=a[first+1],a[first]
       
    p1=a[first]
    p2=a[first+1]
    a.pop(first+1)                            #index of p1 won't be affected by p2
    i = first + 1      
    pivot = p1

    for j in range(first,last) : #Iterate over the remaining array
        if (a[j] < pivot):
            a[i], a[j] = a[j], a[i] #Swap the values
            i = i+1 #Increment i


    pos = i - 1
    
   
    a.append(p2)
    k=first-1
    pivot=a[last]
    for j in range(first , last):  
        if   a[j] < pivot:
            k = k+1
            a[k],a[j] = a[j],a[k]
            
    a[first], a[pos] =  a[pos], a[first]
    a[k+1],a[last] = a[last],a[k+1]
    return pos,( k+1 )
   
    
def quickSort(arr,low,high):
    if low >= high:
        return
    print(a)
    l,r = partition(a,low,high)
    
    print(l,r)
    quickSort(arr, low, l-1)
    quickSort(arr,l+1,r-1)
    quickSort(arr, r+1, high)



quickSort(a,0,len(a)-1)
print(a)


   