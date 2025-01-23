age = 25
print(f"Age: {age},type: {type(age)}")

h = 2.2
print(f"height: {h}, type: {type(h)}")

name = "naman"
print(f"height: {name}, type: {type(name)}")

is_student = True
print(f"height: {is_student}, type: {type(is_student)}")

f = {"apple","banana","cheery"}
print(f"list: {f}, type: {type(f)}")

c = {10.2, 10.3}
print(f"tuple: {c}, type: {type(c)}")

unique = {1,2,3}
print(f"height: {unique}, type: {type(unique)}")

dic = {"name: ": "naman", "age: ":23,"student":True}
print(f"height: {dic}, type: {type(dic)}")

# type conversion

# int to str
age_s = str(age)
print(f"Age: {age_s},type: {type(age_s)}")

# float to str
h_s = str(h)
print(f"height: {h_s}, type: {type(h_s)}")

# list to set
f_s = set(f)
print(f"list: {f_s}, type: {type(f_s)}")