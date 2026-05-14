names = ["Arsh", "Gov", "Isaac"]

names.append("Johann")

print(names)

print(names.sort())

for name in names:
    print(name)

list = [1,2,3,4,5]
list.append(1)
list.insert(2, 5)
list.remove(5)
list.pop()

print(list)

list.clear()
for num in enumerate(list):
    print(list)

if list == names:
    pass

print(len(list))

print(names[0])
combined_lists = list + names
names.index("Arsh")
text = "Hello World"
new_list = text.replace("World", "Hello")
