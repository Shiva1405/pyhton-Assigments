l=['a','e','i','o','u']
l1=[0,0,0,0,0]
l2=[]
r=str(input("enter the scentence"))
for i in r:
  if i in "aeiou":
    l2.append(i)
    l1[l.index(i)]+=1 
print("vowel in a scentence"+str(l2))
print("each vowel repeated as"+str(l1))