
# try , catch
try:
    with open("test.txt", 'r') as reader: #test.txt will pass any other filename will not
        reader.read()

except Exception as e: #catches the error and stores it in a variable
    print(e)


# except:  #print a specific fail message
#     print("Failure Message")

finally:                #use only with try/catch
    print("Cleaning up test records")
