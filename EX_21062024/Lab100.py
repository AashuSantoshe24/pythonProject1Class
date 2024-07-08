#Ductionary
#Key value pair

#name -> "Shraddha" #here name is key value is ashraddha

my_dict = {"name":"Shraddha",
           "age":29,
           "address":"Bangalore"
           }

print(len(my_dict))
print(my_dict["name"])
my_dict["name"] = "Sasha"
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["address"])

phone_book = dict(name="amit", age=57, Address="Delhi")
print(phone_book)