#Normal import
import pack1.A as kohli
print(kohli.a) #1000
kohli.f1()
print("------------------------")
#from import
from pack1.B import b,f2
print(b)
f2()
print("-----------------------------------------")
#Accessing subpack
import pack1.subpack1.C as rohith
print(rohith.b)
rohith.f3()




