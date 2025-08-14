#store following word meaning in a python dictionary
#table: "a piece of furniture","list of facts"
#cats: "a small animall"

# dict= {
#     "cats" : "a small animall",
#     "table" : ["a piece of furniture", "list of facts"]
# }
# print(dict)

#wap to program of given a list of subject for students.one classroom is required for one subject.how many classroom are needed.

# sub={"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(sub))

#wap to enter marks of 3 sub from the user and store them in a dict.start with an empty dict & add one by one.use subject name as key & marks as value

# marks={}
# marks.update({"Math" : 90 , "Physics": 85 , "Chemistry": 92})
# print(marks)

#or with input func

# marks ={}
# a=int(input("math num="))
# b=int(input("phy num="))
# c=int(input("chem num="))
# marks.update({"Math" : a , "Physics": b, "Chemistry" : c})
# print(marks)

#figure out a way to store 9 & 9.0 as separate values in the set

# a={9, "9.0"}
# print(a)

#or pair kore eksathe kora jabe

# a={
#     ("int",9),("float",9.0)
# }
# print(a)


