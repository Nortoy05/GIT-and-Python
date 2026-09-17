print("========= Itereable Objects ============")

# Iterable objects -> String ,dict, tuple,list,range, map, filter

range_obj=range(3) #(0,3)
print("range_obj: ", range_obj)

for ele in range_obj:
    print("the element: ", ele)

text="MIT"
for letter in text:
    print(f"the letter: {letter}" )


print("========= Dictionary objects ============")

# Dictionary is json object
person={"name":"Json","age":25,"single":True}
print("Person :", person)
person_obj=dict(name="Justin ", age=25, single=True)
print("Print_obj: ",person_obj)

#method: get()
name=person_obj.get("name")
hobby= person_obj.get("hobby")
#name=person_obj["name"]
print(f"The name : {name} , The hobby: {hobby}")

del person_obj["single"]


for key in person_obj:
    print(f"The key: {key}")