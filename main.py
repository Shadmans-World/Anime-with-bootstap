

# a = "i am a boy. who is a student of CSE"

# print(a.split())
# #print(a.upper())
# print(a.capitalize())

# print(a.split("s"))


# frst_name = "Shadman Shoumik"
# last_name = "Shaon"

# print(f"Full name is {frst_name} {last_name}")
# print(f"First name is {frst_name}")
# print(f"Last name is {last_name}")

# a = 10
# b = 10

# c = a+b

# print(c)

# print(type(a))


#..............................................
# a= [1,2,3,4,5,6,7,8,9,10,11]

# print(a)

# b = 12
# a.append(b)
# print(a)

# a.pop(5)
# print(f"After removing:{a}")


#..............................................
# a = [5,2,6,67,67754,24,1,46,3,334,56]
# a.sort()
# print(a)
# a.reverse()
# print(a)
# a.remove(6)
# print(a)







#.........................................................DICTIONARIES.........................................................

#myself = {"Name":"Pk","Age":"23","Job":"Student","Earning":"NO","Cell_NO":"01788172639"}
# print(myself.values())
# print(myself.keys())
# print(myself.items())
# print(myself["Name"])
# #Adding a new key & value!!!!!!!!!!!!!!!!!!!!!!!!!!!
# myself["Gender"] = "Male"
# print(myself)

#........................................................Dictionaries-----Dictionaries.........................................................
# dict={"dict_1":{"dict_2":"200"}}
# print(dict)
# print(dict["dict_1"]["dict_2"])


# print(3<2 and 2 == 2)
# print(3<2 or 2 == 2)



'''mylist = [1,2,3,4]

for item in mylist:
    print(item)'''




# try:
#     a = "10"
#     b = 2
#     print(a**b)    

# except TypeError:
#     print("HEY LOOK! Wrong man wrong.....TypeERROR")

# finally:
#     print("Refresh The page. Or input the correct type.")










#..............................................................OOP........................................................

# class Sample():
#     species = "Human"
#     def __init__(self,name,id,classroom):
#         self.name = name
#         self.id = id
#         self.classroom = classroom

    
# x = Sample(name="PK",id="123",classroom="3")
# print(x.name)
# print(x.id)
# print(x.classroom)
# print(Sample)
# print(f"The name is {x.name}. Id is {x.id},Classroom No {x.classroom}\n He is a {x.species}")



# class Squaretangle():
#     def __init__(self,square):
#         self.square = square
#     def area(self):
#         return self.square*self.square
# a = Squaretangle(square=25)
# print(a.area())


#......................................OOP Inheritance.......................................

# class Person:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname

#     def hello(self):
        
#         print("hello")
       
    
#     def report(self):
#         print(f"I am {self.fname} {self.lname}")

# # x = Person("Shaon","Pk")
# # x.hello()
# # x.report()

# class Agent(Person):

#     def __init__(self,fname,lname,cname):
#         Person.__init__(self,fname,lname)
#         self.cname = cname

    

#     def report(self): #Overwrite
#         print("I am here") 

#     def reveal(self,passcode):

#         if passcode == 123:
#             print("I am a secret agent")
#         else:
#             self.report()

    
            
# x =Agent("Shadman","Shaon","Pk")
# x.reveal(123)
# x.hello()
# print(x.cname)
# x.cname



'''from email import message


def myfunc():
    print("i am using my function")

class myclass():
    def __init__(self,message):
        self.message = message
    def report(self):
        print(self.message)'''



