sentence = input("Enter the sentence ")
#taking Sentence as an input string for storing the input from thr user
l=list(sentence)
#converted string into list 
vowels=["a","e","i","o","u"]
#taking vowels in a list 
a,e,i,o,u=0,0,0,0,0
n=len(l)
#taking the length of list of string

for j in range(0,n):
    if l[j]=='a' or l[j]=="A":
        a=a+1
    if l[j]=='e' or l[j]=="E":
        e=e+1
    if l[j]=='i' or l[j]=="I":
        i=i+1 
    if l[j]=='o' or l[j]=="O":
        o=o+1        
    if l[j]=='u' or l[j]=="U":
        u=u+1
#used "for" loop for checking each variable in the list with the vowels 
vowelcount=[]
#list for vowel count 

if a>0:
    vowelcount.append(a)
else:
    vowels.remove("a")
if e>0:
    vowelcount.append(e)
else:
    vowels.remove("e")
if i>0:
    vowelcount.append(i)
else:
    vowels.remove("i")
if o>0:
    vowelcount.append(o)
else:
    vowels.remove("o")
if u>0:
    vowelcount.append(u)
else:
    vowels.remove("u")
#checked the values of the vowels and used remove function to remove an vowel not present in the list
print("Vowels in sentence---",vowels)
print("Each vowel repeated as:-",vowelcount)
        
        
