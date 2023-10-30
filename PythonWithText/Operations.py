# We will perform file operations here
# file = open('new.txt', 'w+')
# file.write("Hello! Universe")
# content = file.read()
# print("Content of the file", content)
# file.close()

# file = open('new.txt', 'r')
# content = file.read()
# print(content)
# file.close()

with open('new.txt', 'r+') as file:
    content = file.readlines()
    print(content)