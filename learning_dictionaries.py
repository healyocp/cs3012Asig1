

#A dictionary is a collection which is unordered,
#changeable and indexed. In Python dictionaries are written with curly brackets,
#and they have keys and values.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


x=thisdict.get("model")
print (x)

for x in thisdict:
    print(x)

for x in thisdict.values():
    print(x)

for x,y in thisdict.items():
    print (x,y)
