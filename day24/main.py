# file=open("my_text.txt")
# content=file.read()
# print(content)
# file.close()

# if we want to not close it manually then we can use 
# with open("my_text.txt") as files:
#     content=files.read()
#     print(content)
# with open("my_text.txt",mode="w") as file:
#     file.write("hello my name is Krishna")
# with open("my_text.txt",mode="a")as file:
#     file.write(" Saini")
#  this is the file path of a text file and we are goona use it to open the file
file_path = r"D:\pythan\day24\219 Solution-snake-game-high-score-final\data.txt"
#  generating new file  only work for write mode
with open("my_new_text.txt",mode="w") as file:
    file.write("hello my name is Krishna")
with open(f"{file_path}",mode="r") as file:
    content=file.read()
    print(content)
# working finee 