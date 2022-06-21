
# try , catch
try:
    with open("test.txt", 'r') as reader: #test.txt will pass any other filename will not
        reader.read()

except:
    print("this is a customized error message if the test fails")