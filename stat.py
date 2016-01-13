
nom1="sisi"
nom2="sese"
import fileinput
l1=[]
for line in fileinput.input(nom1):
    l1.append(line[0:-1])
l2=[]
for line in fileinput.input(nom2):
    l2.append(line[0:-1])
print(" pour ",nom1)
i=1
dico={}
for p in l1:
    dico[p]=i
    print(i,p)
    i+=1
print(" pour ",nom2)
i=1
for p in l2:
    dico[p]=(dico[p]+i)/2
    print(i,p)
    i+=1

print("recapitulatif:")
l=list(dico.items())
l.sort(key=lambda s:s[1])
for ll in l:
    print(ll[0],ll[1])


