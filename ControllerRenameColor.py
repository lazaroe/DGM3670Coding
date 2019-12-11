#ColorNodesControlls
import maya.cmds as cmds
import tokenize as token

def RenameContrl(copyname, ToName):
    splitt = copyname.split("_")
    newname = ""
    
    for sp in range(len(splitt)- 1):
        newname += splitt[sp] + "_"
        
    newname += ToName
    return (newname)
       
def colorControl(Nameof, Type, colorname):
    sels = cmds.ls(sl=True)
    SizeofSelection = len(sels)

    if colorname == 'yellow':
        color = 17
    elif colorname == 'blue':
        color = 6
    elif colorname == 'Red':
        color = 13
    elif colorname == 'Green':
        color = 26
    else:
        color = 5
        
    if SizeofSelection < 1:
        Cirr = cmds.circle(c= (0, 0, 0), name=(Nameof))
        shapes = cmds.listRelatives(Cirr, children = True, shapes = True)
        
        for shape in shapes:
            cmds.setAttr('%s.overrideEnabled' % shape, True)
            cmds.setAttr('%s.overrideColor' % shape, color)
            
    #RENAME
    
    if Type == "Group":
        
        if SizeofSelection < 1:
            print ("Set a default one")
            
        else:
            dups = cmds.duplicate(sels)
            dups = cmds.polyUnite(dups)
            cmds.delete(dups, constructionHistory=True)
            BoxLimits = cmds.xform(dups[0], query=True , boundingBox=True)
            cmds.delete(dups[0])
            XDirect = ((BoxLimits[0]) + (BoxLimits[3])) /2
            YDirect = ((BoxLimits[1]) + (BoxLimits[4])) /2
            ZDirect = ((BoxLimits[2]) + (BoxLimits[5])) /2
            Cirr = cmds.circle(c= (XDirect, YDirect, ZDirect), name=("Group " + Nameof))
            shapes = cmds.listRelatives(Cirr, children = True, shapes = True)
            
            for shape in shapes:
                cmds.setAttr('%s.overrideEnabled' % shape, True)
                cmds.setAttr('%s.overrideColor' % shape, color)
        
    if Type == "Single":
        
        if SizeofSelection < 1:
            print ("Set a default one")
            
        else:
            for i in range(len(sels)):
                BoxLimits = cmds.xform(sels[i], query=True, worldSpace=True, boundingBox=True)
                XDirect = ((BoxLimits[0]) + (BoxLimits[3])) /2
                YDirect = ((BoxLimits[1]) + (BoxLimits[4])) /2
                ZDirect = ((BoxLimits[2]) + (BoxLimits[5])) /2
                Cirr = cmds.circle(c= (XDirect, YDirect, ZDirect), name=RenameContrl(sels[i],Nameof))
                shapes = cmds.listRelatives(Cirr, children = True, shapes = True)
                
                for shape in shapes:
                    cmds.setAttr('%s.overrideEnabled' % shape, True)
                    cmds.setAttr('%s.overrideColor' % shape, color)
                
    else:
        print("no objects selected, will put one in at default")

            
colorControl("Ctrl","Single", 'Green')

            
            
            
            
            
            
            
        