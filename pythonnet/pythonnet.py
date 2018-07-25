import clr
clr.FindAssembly("class1.dll")
from ClassLibrary1 import *

o = Class1()
print(o.Add(5, 6))

# exception
try:
    print(o.Add(-5, 6))
except Exception as e:
    print(e.Message)
