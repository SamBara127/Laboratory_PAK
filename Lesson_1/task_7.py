import os


def open_dir(pathes, level):
    fil = []
    fil += os.listdir(path=pathes)
    os.chdir(pathes)
    for i in range(len(fil)):
        for o in range(level):
            print(" ", end = "")
        if os.path.isdir(fil[i]) == True:
            print("dir -> " + fil[i])
            open_dir(fil[i], level + 1)
        else:
            print("file -> " + fil[i])
    return fil


print("Введите путь каталога: ", end = '')
p = input() 
if os.path.exists(p) != True:
     print("Такого пути или директории не существует. ")
     exit()
open_dir(p, 1)
