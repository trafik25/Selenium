#tuples are protected, they are immutable

#Tuples with multiple datatypes
multiTuple = ("This is a string", 1)
print(multiTuple)

#Lists have brackets, Tuples do not and cannot be changed
#if you want to change a tuple it needs to be made into a list [ ]
#[list] (tuple)
val = [1,2,"Thomas", 56, 67]
print(val[2])

val[2] = "Greg"
print(val)