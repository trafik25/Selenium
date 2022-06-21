str0 = "ThisisThomas.com"
str1 = "from Detroit"
str2 = "Detroit is my hometown"

print(str0[1])   #indexing a string and a value within the string
print(str0[0:5])
print(str0 + ' ' + str1) #concat

print(str1 in str2) #checking for a word within a string

var = str.split(str0)
print(var)
print(var[0])

str5 = " thomas"
print(str5.strip())
