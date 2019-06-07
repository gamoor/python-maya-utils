import maya.cmds as mc

list = mc.ls(selection=True)
prefix = ""
suffix = ""
findReplace = True
find = "L"
replace = "R"

for node in list:
    name = node
    newName = prefix + node + suffix
    #newName = "pop"  
    print newName
    mc.rename(node, newName)
    
if findReplace == True:
    for node in list:
        name = node
        newName = name.replace(find, replace)
        mc.rename(node, newName)