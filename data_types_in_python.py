i=20
type(i)
x= float(i)
y= complex(i) 
z= str(i) 
print(i) 
print(x) 
print(y)
print("this is the string value of i "+z)


s1="Alex" 
s2="Zender"
print(s1 +" "+ s2) 
print(s1[0:1])
print(s2[1:3])


lst=[1,2,900,80.90,"hello"]
print(lst*2) 
lst[2]=90 
print(lst) 
del(lst[2]) 
print(lst)
 
t=(1.2,200,"hello",20)
print(t*2)
'''del(t[2])'''
t2=(1,29,(20+2j,30.9))
print(t2) 
print(t2[2])
t3=(1,29,[20+2j,30.9])
print(type(t3[2])) 
t3[2][0]=19+3j
print(t3)
