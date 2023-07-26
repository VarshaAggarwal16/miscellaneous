items = ["one", "two", "three"]

for item in  [ "one", "two", "three" ]:
    f = open (item + " hello_world.txt", "w")
    f.write("This is my first line of code")
    f.write("\nThis is my second line of code with " + item  + " the first item in my list")
    f.write ("\nAnd this is my last line of code")
    f.close()
