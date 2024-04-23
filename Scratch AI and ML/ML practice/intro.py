 

def doIt():   
    a = [1,3,4,5] 
    for i in a:
        print(i)
    

doIt()

a = [1,2,3,45,6,7,8,9,]

for i in a:
    
    for j in len(a)-1:
        if(a[j] > a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print(a)

