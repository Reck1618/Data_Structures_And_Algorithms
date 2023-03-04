# Merge Storted Arrays to return a Sorted Array.
a=[1,2,3,4]
b=[3,7,9,12]

def merge(a,b):
    ans = []
    i = 0
    j = 0

    if len(a) == 0 or len(b) == 0:
        return a + b
    
    while i < len(a) and j < len(b):

        if a[i] <= b[j]:
            ans.append(a[i])
            i += 1
        
        else:
            ans.append(b[j])
            j += 1
        
    return ans + a[i:] + b[j:]

print(merge(a,b)) 