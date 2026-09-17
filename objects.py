''' OBJECTS

1->What is object
2->Iterable objects & Range
3->Dictionary
4-> Error handling system

'''

import array
import math
print("========= What is object ============")
from math import ceil ,asin


print(type ('Hello Wrold '))
print(type(100))
print(type(True))
print(type(array))
print(type(math))


# OOP 4 concepts-> Abstraction | Encapsulation | Inheritance | Polimorphism
result1=math.ceil(97.7) 
print(f"Result1:  {result1}")


print("========= Error handling system ============")

car_dict=dict(name="Tayota", year=(2026), electric=True)


try:
    print("Passed here")
    a=car_dict.speed
    result=car_dict["origin"]
    print("Result: ", result)
except KeyError as err:
    print("No origin state property found: ",err)
except AttributeError as err:
    print("No speed found: ",err)
except Exception as err:
    print("General error: ",err)
else:
    print("Executed succesfully without errors")
finally:
    print("Final closing logic")