Name = "penguin"
Age = 10
is_student = True
weight = 34.5

print("name:", Name)
print("data type of name:", type(Name))
print("age:", Age)
print("data type of age:", type(Age))
print("is_student:", is_student)
print("data type of is_student:", type(is_student))
print("weight:", weight)
print("data type of weight:", type(weight))
print("\n after type casting :")
Age = str(Age)
is_student = str(is_student)
weight = str(weight)
print("data type of age after type casting:", type(Age))
print("data type of is_student after type casting:", type(is_student))
print("data type of weight after type casting:", type(weight))