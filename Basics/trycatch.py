
# try , catch
try:
    with open("filelog.txt", 'r') as reader:
        reader.read()

except:
    print("this is a block--failed test")