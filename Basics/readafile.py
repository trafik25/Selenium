
file = open('test.txt')
#print(file.read()) # read all chars
#print(file.read(5)) #read up to 5 chars
# do not mix read and readline

#print(file.readline()) #prints 1st line
#print(file.readline())  #prints 2nd line

#print line by line using realine method
# line = file.readline()
# while line!="":
#     print((line))
#     line = file.readline()

#var = ["abc", "etir", 'erret', 'tyt']
for line in file.readlines():
    print(line)
file.close()  #always last for reading lines in text file