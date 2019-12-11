#ToolBox
import maya.cmds as cmds
import tokenize as token
import random

class Toolbox():
    def __init__(self):
        self.window_name = "mnToolbox"

    def create(self):
        self.delete()

        #RANDOM GENERATOR
        self.window_name = cmds.window(self.window_name)
        self.m_column = cmds.columnLayout(parent= self.window_name, adjustableColumn=True)
        cmds.rowColumnLayout(parent= self.m_column, numberOfColumns=1)
        cmds.text(label='Random Placement Generator: ')
        cmds.rowColumnLayout(parent= self.m_column, numberOfColumns=4)
        cmds.text(label=' (Amount) ')
        self.AmountOf = cmds.intField()
        cmds.text(label=' (Min) ')
        self.minDistance = cmds.intField()
        cmds.rowColumnLayout(parent= self.m_column, numberOfColumns=4)
        cmds.text(label=' (Max) ')
        self.maxdistance = cmds.intField()
        cmds.text(label=' (SkyLimit) ')
        self.SkyLimit = cmds.intField()
        cmds.button(label='GroundGen', command=lambda *args: self.LandscapeGen("Ground",cmds.intField(self.AmountOf, query=True, value= True), cmds.intField(self.minDistance, query=True, value= True), cmds.intField(self.maxdistance, query=True, value= True), cmds.intField(self.SkyLimit, query=True, value= True)))
        cmds.text(label=' or ')
        cmds.button(label='SkyGen', command=lambda *args: self.LandscapeGen("Sky",cmds.intField(self.AmountOf, query=True, value= True), cmds.intField(self.minDistance, query=True, value= True), cmds.intField(self.maxdistance, query=True, value= True), cmds.intField(self.SkyLimit, query=True, value= True)))
        
        #LOCATOR TOOL
        cmds.rowColumnLayout(parent= self.m_column, numberOfColumns=5)
        cmds.text(label='Center Locator Tool: ')
        cmds.button(label='Group', command=lambda *args: self.CenterLocator("Group"))
        cmds.text(label=' or ')
        cmds.button(label='Single', command=lambda *args: self.CenterLocator("Single"))
        cmds.text(label='((Make sure you select multiple objects))')
        
        #COLOR ASSIGNEMENT
        cmds.rowColumnLayout(parent= self.m_column, numberOfColumns=3)
        cmds.text(label='Color Assignment: ')
        self.color = cmds.colorIndexSliderGrp(min=2,max=32)
        cmds.button(label='Change Color', command=lambda *args: self.colorBtn())
        
        #RENAME TOOL
        cmds.rowColumnLayout(parent= self.m_column, numberOfColumns=5)
        cmds.text(label='Sequential Renamer Tool: ')
        self.name = cmds.textField()
        cmds.text(label='###')
        self.nametwo = cmds.textField()
        cmds.button(label='Rename', command=lambda *args: self.RenameTool(cmds.textField(self.name, query=True, text= True), cmds.textField(self.nametwo, query=True, text= True)))
        
        #CREATE CONTROL
        cmds.rowColumnLayout(parent= self.m_column, numberOfColumns=7)
        cmds.text(label='Create Control')
        self.Nameof = cmds.textField()
        cmds.text(label='<- Name of Control ')
        self.ColorName = cmds.colorIndexSliderGrp(min=2,max=32)
        cmds.button(label='Group', command=lambda *args: self.colorControl(
        cmds.textField(self.Nameof, query=True, text= True),"Group",
        cmds.colorIndexSliderGrp(self.ColorName, query=True,value=True)-1))
        cmds.text(label=' or ')
        cmds.button(label='Single', command=lambda *args: self.colorControl(
        cmds.textField(self.Nameof, query=True, text= True),"Single",
        cmds.colorIndexSliderGrp(self.ColorName, query=True,value=True)-1))
        
        
        
        
        #CALCULATOR
        cmds.text(parent=self.m_column, label='Calculator Val [0,0]')
        self.values = cmds.textField(parent=self.m_column)       
        cmds.button(parent=self.m_column,label="Add",command=lambda *args: self.AddBut())
        cmds.button(parent=self.m_column,label="Subtract",command=lambda *args: self.SubBut())
        cmds.button(parent=self.m_column,label="Multiply",command=lambda *args: self.MultiplyBut())
        cmds.button(parent=self.m_column,label="Divide",command=lambda *args: self.DivideBut())
        cmds.button(parent=self.m_column,label="Mean",command=lambda *args: self.MeanBut())
        cmds.button(parent=self.m_column,label="Median",command=lambda *args: self.MedianBut())
        cmds.button(parent=self.m_column,label="Mode",command=lambda *args: self.ModeBut())
        
        cmds.rowColumnLayout(parent= self.m_column, numberOfColumns=3)
        self.Numberone = cmds.intField()
        self.Numbertwo = cmds.intField()
        cmds.button(label="Power",command=lambda *args: self.Power(cmds.intField(self.Numberone, query=True, value= True), cmds.intField(self.Numbertwo, query=True, value= True)))
        
       
        #cmds.button(parent=self.m_column,label="Yellow",command = lambda *args: self.colorControl('yellow'))
        cmds.showWindow(self.window_name)

    def delete(self):
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name)
            
            #CALCULATOR BUTTONS
    def AddBut(self):
        something = Toolbox()
        values = cmds.textField(self.values, query=True, text= True)
        temp = values.split(",")
        expi = list()
        for com in range(len(temp)):
            expi.append(float(temp[com])) 
        print something.Add(expi)
        
    def SubBut(self):
        something = Toolbox()
        values = cmds.textField(self.values, query=True, text= True)
        temp = values.split(",")
        expi = list()
        for com in range(len(temp)):
            expi.append(float(temp[com])) 
        print something.Subtract(expi)
        
    def MultiplyBut(self):
        something = Toolbox()
        values = cmds.textField(self.values, query=True, text= True)
        temp = values.split(",")
        expi = list()
        for com in range(len(temp)):
            expi.append(float(temp[com])) 
        print something.Multiply(expi)
        
    def DivideBut(self):
        something = Toolbox()
        values = cmds.textField(self.values, query=True, text= True)
        temp = values.split(",")
        expi = list()
        for com in range(len(temp)):
            expi.append(float(temp[com])) 
        print something.Divide(expi)
        
    def MeanBut(self):
        something = Toolbox()
        values = cmds.textField(self.values, query=True, text= True)
        temp = values.split(",")
        expi = list()
        for com in range(len(temp)):
            expi.append(float(temp[com])) 
        print something.Mean(expi)
        
    def MedianBut(self):
        something = Toolbox()
        values = cmds.textField(self.values, query=True, text= True)
        temp = values.split(",")
        expi = list()
        for com in range(len(temp)):
            expi.append(float(temp[com])) 
        print something.Median(expi)
        
    def ModeBut(self):
        something = Toolbox()
        values = cmds.textField(self.values, query=True, text= True)
        temp = values.split(",")
        expi = list()
        for com in range(len(temp)):
            expi.append(float(temp[com])) 
        print something.Mode(expi)
                 
    #ENDING OF CALCULATOR
    def colorBtn(self):
        value = cmds.colorIndexSliderGrp(self.color, query=True, value= True) -1
        self.ChangeColor(value)
        
    #RENAME
    def RenameTool(self,nameType,nodeTypee):
        numberType = str()
        numberLoop = str()
        objName = (nameType) + "###" + (nodeTypee)
        sels = cmds.ls(sl=True)
        strings = objName.split("#")
        chars = len(objName) - len(strings[0]) - len(strings[len(strings)-1])
        print (chars)
    
        for i in range(0, len(sels)):
            numberType = str()
            numberLoop = str(i + 1)
        
            for j in range(chars - len(numberLoop)):
                numberType += str("0")
            numberType += str(i + 1)
            cmds.rename(sels[i], (strings[0] + "_" + numberType + "_" + strings[len(strings)-1]))
            
    #LOCATOR
    def CenterLocator(self,Type):
        selection = cmds.ls(sl=True)
        SizeofSelection = len(selection)
        
        if Type == "Group":
            dups = cmds.duplicate(selection)
            dups = cmds.polyUnite(dups)
            cmds.delete(dups, constructionHistory=True)
            BoxLimits = cmds.xform(dups[0], query=True , boundingBox=True)
            cmds.delete(dups[0])
            XDirect = ((BoxLimits[0]) + (BoxLimits[3])) /2
            YDirect = ((BoxLimits[1]) + (BoxLimits[4])) /2
            ZDirect = ((BoxLimits[2]) + (BoxLimits[5])) /2
            cmds.spaceLocator(position= (XDirect, YDirect, ZDirect), name=("Locator"))
        
        if Type == "Single":
            for i in range(len(selection)):
                BoxLimits = cmds.xform(selection[i], query=True, worldSpace=True, boundingBox=True)
                XDirect = ((BoxLimits[0]) + (BoxLimits[3])) /2
                YDirect = ((BoxLimits[1]) + (BoxLimits[4])) /2
                ZDirect = ((BoxLimits[2]) + (BoxLimits[5])) /2
                cmds.spaceLocator(position= (XDirect, YDirect, ZDirect), name=("Locator" + str(i)))
            
    #LANDSCAPE
    
    def LandscapeGen(self, type, Amount, minDistance, maxdistance,SkyLimit):
        from random import randint
        sels = cmds.ls(sl=True)
        Min = random.randint(minDistance, 0)
        Max = random.randint(0, maxdistance)
        SkyLim = random.randint(minDistance, SkyLimit)
        SkyMax = random.randint(SkyLimit, maxdistance)
        if type == "Ground":
            for i in range(Amount):
                for l in range(len(sels)):
                    cmds.duplicate(sels[l])
                    randNum = random.randint(Min, Max)
                    randNumz = random.randint(Min, Max)
                    cmds.move(randNum, 0, randNumz, sels[l])
                
        if type == "Sky":
            for i in range(Amount):
                for l in range(len(sels)):
                    cmds.duplicate(sels[l])
                    randNum = random.randint(Min, Max)
                    randNumz = random.randint(Min, Max)
                    SkyNum =  random.randint(SkyLim, SkyMax)
                    cmds.move(randNum, SkyNum, randNumz, sels[l])
                          
    #COLOR CONTROL
    def ChangeColor(self, colorindex):
        sels = cmds.ls(sl=True)
        for sel in sels:
            shapes = cmds.listRelatives(sel, children=True, shapes=True)

            for shape in shapes:
                cmds.setAttr('%s.overrideEnabled' % shape, True)
                cmds.setAttr('%s.overrideColor' % shape, colorindex)
                
    #CALCULATOR           
    def Add(self,values):
        sum = 0
        for val in values:
            sum = sum + val
           
            print sum

    def Subtract(self,values):
        Sub = values[0]
        for val in range(1,len(values)):
            Sub -= values[val]
            print Sub


    def Multiply(self,values):
        Mul = 1
        for val in values:
            Mul = Mul * val
            print Mul
        
    def Divide(self,values):
        Div = values[0]
        for val in range(1,len(values)):
            Div /= values[val]
            print Div

    def Power (self,values,power):
        import math
        print math.pow(values,power)   
        return math.pow(values,power)   

    def Mean(self,values):
        sum = 0
        for val in values:
            sum = sum + val
        mean = sum / len(values) 
        print mean  #The Median and Mode was help from a video on Google.


    def Median(self,values):
        median = sorted(values)[len(values) / 2] #sorting the numbers from lest to greatest
        print median #you are getting the numbers of values in the list, and dividing that number by 2.

    def Mode(self,values):
        mode = max(values, key = values.count) #max returns the largest number. 
        print mode #key means that it gets any indivdual elements and tries to see if there any exactly alike.


    #CREATE CONTROL
    def RenameContrl(self, copyname, ToName):
        splitt = copyname.split("_")
        newname = ""
        
        for sp in range(len(splitt)- 1):
            newname += splitt[sp] + "_"
            
        newname += ToName
        return (newname)
           
    def colorControl(self, Nameof, Type, colorname):
        sels = cmds.ls(sl=True)
        SizeofSelection = len(sels)
        
     
        if SizeofSelection < 1:
            Cirr = cmds.circle(c= (0, 0, 0), name=(Nameof))
            shapes = cmds.listRelatives(Cirr, children = True, shapes = True)
            
            for shape in shapes:
                cmds.setAttr('%s.overrideEnabled' % shape, True)
                cmds.setAttr('%s.overrideColor' % shape, colorname)
                
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
                    cmds.setAttr('%s.overrideColor' % shape, colorname)
            
        if Type == "Single":
            
            if SizeofSelection < 1:
                print ("Set a default one")
                
            else:
                for i in range(len(sels)):
                    BoxLimits = cmds.xform(sels[i], query=True, worldSpace=True, boundingBox=True)
                    XDirect = ((BoxLimits[0]) + (BoxLimits[3])) /2
                    YDirect = ((BoxLimits[1]) + (BoxLimits[4])) /2
                    ZDirect = ((BoxLimits[2]) + (BoxLimits[5])) /2
                    Cirr = cmds.circle(c= (XDirect, YDirect, ZDirect), name=self.RenameContrl(sels[i],Nameof))
                    shapes = cmds.listRelatives(Cirr, children = True, shapes = True)
                    
                    for shape in shapes:
                        cmds.setAttr('%s.overrideEnabled' % shape, True)
                        cmds.setAttr('%s.overrideColor' % shape, colorname)
                    
        else:
            print("no objects selected, will put one in at default")

            

myTool = Toolbox()
myTool.create()
    
    