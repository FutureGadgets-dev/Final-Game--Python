#revamp menu

#Mainmenu
#Abdullahi Jama and Ahmad Kashash

#startscreen:cant get back here
#choosing page: practice, multiplayer, settings
    #[practice, multiplayer]
        #character selection
        #map selection
        #time limit stuff
    #setting
        #powerup drops
        #sound
        #and controls

from pygame import *
from random import *
from math import*
import os

##init () #initializes the mixer music into python pygame
##mixer.music.load ("Super Smash Bros Brawl -Main Menu Theme- (In HD).mp3")  #loads and plays the music 
##mixer.music.play ()

screen=display.set_mode((800,600))


menu=image.load("Menu1.png")

mainmenu=transform.scale(menu,(800,600))



class Picker:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.Rect=Rect(x+20,y,x+40,y+20)

def start():
    running = True
    startscreen=image.load("Super-Smash-Bros-Brawl-1073722.jpg")
    startscreen = transform.smoothscale(startscreen, screen.get_size())
    screen.blit(startscreen,(0,0))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[K_SPACE] == 1: running = False
        display.flip()
    return "menu"

hand=image.load("hand.png")
hand2 = image.load("hand 2.png")
cursorList=[]

def cursormove(pic,cursor1,cursor2):
    keys=key.get_pressed()
    screen.blit(hand,(cursor1.x,cursor1.y))
    if keys[K_UP]:
        cursor1.y-=5
    if keys[K_DOWN]:
        cursor1.y+=5
    if keys[K_RIGHT]:
        cursor1.x+=5
    if keys[K_LEFT]:
        cursor1.x-=5
    cursor1.Rect=Rect(cursor1.x,cursor1.y,cursor1.x+20,cursor1.y+20)
    x1 = hand.get_width()
    y1 = hand.get_height()
    handRect = Rect(cursor1.x,cursor1.y,x1,y1)
##    draw.rect(screen,(255,0,0),(handRect))

    if cursor2!="":
        screen.blit(hand2,(cursor2.x,cursor2.y))
        if keys[K_w]:
            cursor2.y-=5
        if keys[K_s]:
            cursor2.y+=5
        if keys[K_d]:
            cursor2.x+=5
        if keys[K_a]:
            cursor2.x-=5
        cursor2.Rect=Rect(cursor2.x,cursor2.y,cursor2.x+20,cursor2.y+20)
        x2 = hand2.get_width()
        y2 = hand2.get_height()
        hand2Rect = Rect(cursor2.x,cursor2.y,x2,y2)
##        draw.rect(screen,(255,0,0),(hand2Rect))
        
def menu():
    battleRect=Rect(40,90,430,179)
    battlepic=image.load("Menu2.png")#40 pixels bigger
    battlepic = transform.scale(battlepic,(835,700))
    optionRect = Rect(415,375,150,130)
    optionpic = image.load("Menu3.png")
    optionpic = transform.scale(optionpic,(750,600))
    dataRect = Rect(600,345,150,150)
    datapic = image.load("Menu4.png")
    datapic = transform.scale(datapic,(750,600))
    option = False
    data = False
    running=True
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"
        keys = key.get_pressed()        
        screen.blit(mainmenu,(0,0))

        mpos=mouse.get_pos()
        mb=mouse.get_pressed()
#--------------------------------------------------------------------------
        if battleRect.collidepoint(mpos):
            screen.blit(battlepic,(battleRect.x-50,battleRect.y-120))
            if mb[0]==1:
                return "character"
#----------------------------------------------------------------------
        if optionRect.collidepoint(mpos):
            screen.blit(optionpic,(optionRect.x-382,optionRect.y-380))
##            option = True
##        else:
##            option = False                          #PROBLEMS HERE
            if mb[0] == 1: #and option == True:
                return "Option"
#---------------------------------------------------------------------------------------
        elif dataRect.collidepoint(mpos):
            screen.blit(datapic,(dataRect.x-560,dataRect.y-345))
##            data = True
##        else:
##            data = False                            #PROBLEMS HERE
            if mb[0] == 1: #and data == True:
                return "Data"
#---------------------------------------------------------------------------------

        display.flip()

p1,p2,p3,p4="","","",""
def character():
    global p1,p2,p3,p4
    running=True
    fmewtwo = image.load("150_mewtwo___bw_style_by_pklucario-d5x7m50.png")
    fmewtwo = transform.scale(fmewtwo,(150,100))

    fkirby = image.load("KRTDL_Kirby_Jump.png")
    fkirby = transform.scale(fkirby,(150,100))

    fdiddy = image.load("Diddy_Kong.png")
    fdiddy = transform.scale(fdiddy,(150,100))

    fzabuza = image.load("3524834-ap89dw.png")
    fzabuza = transform.scale(fzabuza,(150,130))

    smewtwo = image.load("150Mewtwo_AG_anime.png")
    smewtwo = transform.scale(smewtwo,(130,130))
    skirby = image.load("Kirby_Wii.png")
    skirby = transform.scale(skirby,(130,130))
    sdiddy = image.load("Diddy_Kong(Clear).png")
    sdiddy = transform.scale(sdiddy,(130,130))
    szabuza = image.load("zabuza.png")
    szabuza = transform.scale(szabuza,(130,130))
    charselect=image.load("character-selection.jpg")
    charbackpic = image.load("character-selection (1).png")
    charselect=transform.scale(charselect,(800,600))
    charbackpic = transform.scale(charbackpic,(800,600))
    first=Picker(150,400)
    second=""
    back1Rect = Rect(50,0,50,50)
    backfix = False
    characters = [smewtwo,skirby,sdiddy,szabuza]
    cursorList.extend([first,second])  #allows for two lists to be put into on big list (2d list)
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        screen.blit(charselect,(0,0))
        keys = key.get_pressed() #makes a list of the keys on the keyboard

        if keys[K_2] and second=="":
            second=Picker(450,400)
            cursorList[1]=second
        
        x1 = hand.get_width()
        y1 = hand.get_height()
        handRect = Rect(cursorList[0].x,cursorList[0].y,x1,y1)

        if cursorList[1]!="":
            x2 = hand2.get_width()
            y2 = hand2.get_height()
            hand2Rect = Rect(cursorList[1].x,cursorList[1].y,x2,y2)


        screen.blit(fmewtwo,(100,110))
        mewtwoRect = Rect(100,110,150,100)
##        draw.rect(screen,(255,0,0),mewtwoRect)#
        screen.blit(fkirby,(170,240))
        kirbyRect = Rect(170,240,150,100)
##        draw.rect(screen,(255,0,0),kirbyRect)#
        screen.blit(fdiddy,(340,120))
        diddyRect = Rect(340,120,150,100)
##        draw.rect(screen,(255,0,0),diddyRect)#
        screen.blit(fzabuza,(450,230))
        zabuzaRect = Rect(450,220,150,130)
##        draw.rect(screen,(255,0,0),zabuzaRect)#
#---------------------------------------------------------------------------------
        click1 = keys[K_n]
        click2 = keys[K_z]
        click11 = keys[K_t]
        click22 = keys[K_y]

        if mewtwoRect.colliderect(handRect):
            if click1 == 1:
                p1="Mewtwo"
        if kirbyRect.colliderect(handRect):
            if click1 == 1:
                p1="Kirby" 
        if diddyRect.colliderect(handRect):
            if click1 == 1:
                p1="Diddy"  
        if zabuzaRect.colliderect(handRect):
            if click1 == 1:
                p1="Zabuza"
            
        if p1=="Mewtwo":
            screen.blit(smewtwo,(80,380))
        if p1 == "Kirby":
            screen.blit(skirby,(70,385))
        if p1 == "Diddy":
            screen.blit(sdiddy,(70,380))
        if p1 == "Zabuza":
            screen.blit(szabuza,(80,380))
#------------------------------------------------------------------------------------------
        if cursorList[1]!="":
            if mewtwoRect.colliderect(hand2Rect):
                if click2 == 1:
                    p2="Mewtwo"
            if kirbyRect.colliderect(hand2Rect):
                if click2 == 1:
                    p2="Kirby" 
            if diddyRect.colliderect(hand2Rect):
                if click2 == 1:
                    p2="Diddy"  
            if zabuzaRect.colliderect(hand2Rect):
                if click2 == 1:
                    p2="Zabuza"
                
            if p2 =="Mewtwo":
                screen.blit(smewtwo,(250,380))
            if p2 == "Kirby":
                screen.blit(skirby,(250,385))
            if p2 == "Diddy":
                screen.blit(sdiddy,(250,380))
            if p2 == "Zabuza":
                screen.blit(szabuza,(250,380))
#-------------------------------------------------------------------------------
        if mewtwoRect.colliderect(handRect):
            if click11 == 1:
                p3="Mewtwo"
        if kirbyRect.colliderect(handRect):
            if click11 == 1:
                p3="Kirby" 
        if diddyRect.colliderect(handRect):
            if click11 == 1:
                p3="Diddy"  
        if zabuzaRect.colliderect(handRect):
            if click11 == 1:
                p3="Zabuza"
            
        if p3=="Mewtwo":
            screen.blit(smewtwo,(410,380))
        if p3 == "Kirby":
            screen.blit(skirby,(410,385))
        if p3 == "Diddy":
            screen.blit(sdiddy,(410,380))
        if p3 == "Zabuza":
            screen.blit(szabuza,(410,380))
#-------------------------------------------------------------------------------
        if mewtwoRect.colliderect(handRect):
            if click22 == 1:
                p4="Mewtwo"
        if kirbyRect.colliderect(handRect):
            if click22 == 1:
                p4="Kirby" 
        if diddyRect.colliderect(handRect):
            if click22 == 1:
                p4="Diddy"  
        if zabuzaRect.colliderect(handRect):
            if click22 == 1:
                p4="Zabuza"
            
        if p4=="Mewtwo":
            screen.blit(smewtwo,(570,380))
        if p4 == "Kirby":
            screen.blit(skirby,(570,385))
        if p4 == "Diddy":
            screen.blit(sdiddy,(570,380))
        if p4 == "Zabuza":
            screen.blit(szabuza,(570,380)) 
#------------------------------------------------------------------------------------
        if back1Rect.colliderect(cursorList[0].Rect): #or back1Rect.colliderect(hand2Rect):
            backfix = True
            if backfix == True:
                screen.blit(charbackpic,(0,0))
            if click1 == 1:
                return "menu"

##        return[p1,p2,p3,p4]

        if keys[K_RETURN]:#make this if selections are done
            return "maps"
        
        cursormove(hand,first,second)
    
        display.flip()

#------------------------------------------------------------------------------------------
keys = key.get_pressed()
def Option():
    running = True
    controlspic = image.load("options2.jpg")
    controlspic = transform.scale(controlspic,(800,600))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"
        keys = key.get_pressed()
        screen.blit(controlspic,(0,0))
##        cursormove(hand,cursorList[0],cursorList[1])
        if keys[K_ESCAPE] == 1:
            return "menu"
#------------------------------------------------------------------------------------------        
def Data():
    gamedata = image.load("options3.jpg")
    gamedata = transform.scale(gamedata,(800,600))
    running = True
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"
        keys = key.get_pressed()
        screen.blit(gamedata,(0,0))
##        cursormove(hand,cursorList[0],cursorList[1])
        if keys[K_ESCAPE] == 1:
            return "menu"
#------------------------------------------------------------------------------------------        

mapp=""
def maps():
    global mapp
    running=True
    mapselect=image.load("2afxw2g (1).png")
    mapselect=transform.scale(mapselect,(800,600))
    mapbackpic = image.load("2afxw2g (2).png")
    mapbackpic = transform.scale(mapbackpic,(800,600))
    FinalDes = image.load("10445832_658916887528543_2050382375_o.jpg")
    FinalDes=transform.scale(FinalDes,(1260,700))
    FinalDes2 = transform.scale(FinalDes,(250,130))
    SP = image.load("tCk7BSV.jpg")
    SP=transform.scale(SP,(1260,700))
    SP2 = transform.scale(SP,(250,130))
    Dreamland = image.load("hqdefault.jpg")
    Dreamland=transform.scale(Dreamland,(1260,700))
    Dreamland2 = transform.scale(Dreamland,(250,130))
    back2Rect = Rect(0,0,80,80)
    FDrect=Rect(330,60,250,130)
    SPrect=Rect(330,200,250,130)
    DLrect=Rect(330,340,250,130)
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        keys = key.get_pressed()
        x1 = hand.get_width()
        y1 = hand.get_height()
        handRect = Rect(cursorList[0].x,cursorList[0].y,x1,y1)
        screen.blit(mapselect,(0,0))
        screen.blit(FinalDes2,(330,60))
        screen.blit(SP2,(330,200))
        screen.blit(Dreamland2,(330,340))
        click = keys[K_n]
        if back2Rect.colliderect(handRect):
            screen.blit(mapbackpic,(0,0))
            if click == 1:
                return "character"
        if click==1:
            if FDrect.colliderect(handRect):
                mapp=FinalDes
            if SPrect.colliderect(handRect):
                mapp=SP
            if DLrect.colliderect(handRect):
                mapp=Dreamland

        if mapp!="" and keys[K_RETURN]:
            return "game"
        
        cursormove(hand,cursorList[0],cursorList[1])
        display.flip()

#Make AI shoot and fight
#pause goes in the while loop of the game function
def game():
    global p1,p2,p3,p4,mapp
    charPick=[p1,p2,p3,p4]
    screen=display.set_mode((1260,700))
    stage=mapp
    font.init()
    centuryfont= font.SysFont("Century Gothic",70)
    class Character(object):
        vx,vy=0,0
        onGround=True
        kup=True
        fRight= True
        perDamage=0
        lives=3
        pics=[]
        frame=0 
        def __init__(self,x, y, speed, weight, sizex, sizey, numofjump,pic):
            self.x=x
            self.y=y
            self.speed=speed
            self.weight=weight
            self.sizex=sizex
            self.sizey=sizey
            self.numofjump=numofjump
            self.startjump=numofjump
            self.shotList=[]
            self.platRect=Rect(260,440,745,20)
            self.Rect=Rect(self.x,self.y,self.sizex,self.sizey)
            self.paralyze=0
            self.timer=0
            self.paralyzeList=[25,35,45,60,1000]
            self.weightList=[80,0,0,0,0]
            self.distList=[[5,-5],[15,-15],[20,-21],[27,-30],[100,-100]]
            self.pic=pic
            self.pics=picUpload(self.pic)[0]
            
        def move(self,upKey,rightKey,leftKey):
            draw.rect(screen,(111,111,111),self.platRect)
            draw.rect(screen,(255,0,0),self.Rect)
            keys=key.get_pressed()
            if eval(leftKey) or eval(rightKey):
                if self.paralyze<=0:
                    self.frame+=.4
                    if self.frame>len(self.pics):
                        self.frame=0
                    if eval(rightKey):
                        screen.blit(self.pics[int(self.frame)],(self.x,self.y))
                        if self.vx<20*self.speed:
                            self.vx+=self.speed/2
                        self.fRight= True
                    elif eval(leftKey):
                        screen.blit(transform.flip(self.pics[int(self.frame)],1,0),(self.x,self.y))
                        if self.vx>-20*self.speed:
                            self.vx-=self.speed/2                        
                        self.fRight= False
                    self.x+=self.vx
                    self.Rect.x+=self.vx
                
            if eval(rightKey)==False or self.paralyze>0:
                if self.fRight:
                    screen.blit(self.pics[0],(self.x,self.y))
            if eval(leftKey)==False or self.paralyze>0:
                if self.fRight==False:
                    screen.blit(transform.flip(self.pics[0],1,0),(self.x,self.y))

            if eval(rightKey)==False and eval(leftKey)==False:
                if self.vx>0:
                    self.vx-=.6
                    self.x+=self.vx
                    self.Rect.x+=self.vx
                    if self.vx<.6:
                        self.vx=0
                if self.vx<0:
                    self.vx+=.6
                    self.x+=self.vx
                    self.Rect.x+=self.vx
                    if self.vx>-.6:
                        self.vx=0

            if self.paralyze>0:
                if self.vx>0:
                    self.vx-=.4
                    self.x+=self.vx
                    self.Rect.x+=self.vx
                    if self.vx<.4:
                        self.vx=0
                if self.vx<0:
                    self.vx+=.4
                    self.x+=self.vx
                    self.Rect.x+=self.vx
                    if self.vx>-.4:
                        self.vx=0
            #-------------------------------------------------------
            if eval(upKey)==0 and self.paralyze<=0:
                self.kup=True

            if eval(upKey) and self.kup==True and self.numofjump>0 and self.paralyze<=0:  
                self.vy=-13
                self.numofjump-=1
                self.onGround=False
                self.kup=False
                
            self.vy+=0.8*self.weight
            self.y+=self.vy
            self.Rect.y+=self.vy

            if self.Rect.colliderect(self.platRect):
                if self.vy>0:
                    self.numofjump=self.startjump
                    self.y=self.platRect.y-self.sizey
                    self.Rect.y=self.platRect.y-20
                    self.vy = 0
                    self.onGround=True
                if self.vy<0:
                    self.y=self.platRect.bottom
                    self.Rect.y=self.platRect.bottom
                    self.vy = 0

            self.Rect=Rect(self.x,self.y,self.sizex,self.sizey)

            if self.paralyze>0:
                self.paralyze-=1

        def damage(self):
            self.weightList[1]=int(self.perDamage*0.1)
            self.weightList[2]=int(self.perDamage*0.05)
            self.weightList[3]=int(self.perDamage*0.03)
            self.weightList[4]=int(self.perDamage*0.02)
            if self.perDamage>=50:
                self.weightList[1]=int(self.perDamage*0.28)
            if self.perDamage>=100:
                self.weightList[2]=int(self.perDamage*0.24)
            if self.perDamage>=150:
                self.weightList[3]=int(self.perDamage*0.20)
            if self.perDamage>=200:
                self.weightList[0]=int(self.perDamage*.4)
                self.weightList[4]=int(self.perDamage*0.16)

        def position(self):
            return([self.x, self.y, self.Rect])

    class AI(Character): 
        def __init__(self, *args, **kwargs):
            Character.__init__(self, *args, **kwargs)
        def move2(self, targetList):
            keys=key.get_pressed()
            draw.rect(screen,(255,0,0),self.Rect)
            screen.blit(self.pics[0],(self.x,self.y))
            small=False
            rdist=10000
            distList=[]
            for target in targetList:
                if target!=False:
                    dist = max(1,distance(self.x, self.y, target.x, target.y))
                    distList.append(dist)
                    if dist< rdist:
                        small=target
                        rdist=dist
            if small!=False:
                if self.paralyze<=0:
                    if small.x>self.x:
                        self.move("False","True","False")
                    if small.x<self.x:
                        self.move("False","False","True")
                    if small.y<self.y and self.y-small.y>10:
                        self.move("True","False","False")
                if self.paralyze>0:
                    self.paralyze-=1
                    self.move("False","False","False")

    class Shot:
        removeList=[]
        shotKey=True
        pics=[]
        frame=0
        def __init__(self, speed, sizex, sizey, damage, pic):
            self.speed=speed
            self.sizex=sizex
            self.sizey=sizey
            self.shotRect=""
            self.shotList=[]
            self.count=0
            self.pic=pic
            self.pics=picUpload(self.pic)[4]
        def addShot(self,position,fRight,sButton,size):
            keys=key.get_pressed()
            if eval(sButton)==0:
                self.shotKey=True
            if eval(sButton) and self.shotKey==True and self.count==0:
                if fRight==True:
                    self.shotList.append([position[0]+size+1,position[1],True,self.damage,self.shotRect])
                if fRight==False:
                    self.shotList.append([position[0]-self.sizex-1,position[1],False,self.damage,self.shotRect])
                self.shotKey=False
                self.count=30
            if self.count>0:
                self.count-=1
        def moveShot(self):
            for shot in self.shotList:
                shot[4]=Rect(shot[0],shot[1]-self.sizey,self.sizex*2,self.sizey*2)
                draw.rect(screen,(255,0,0),shot[4])
                self.frame+=0.1
                if self.frame>len(self.pics):
                    self.frame=0
                if shot[2]==True:
                    shot[0]+=self.speed
                    screen.blit(self.pics[int(self.frame)],(shot[4]))
                    if shot[0]>1260:
                        self.removeList.append(shot)
                if shot[2]==False:
                    shot[0]-=self.speed
                    screen.blit(transform.flip(self.pics[int(self.frame)],1,0),shot[4])
                    if shot[0]<0:
                        self.removeList.append(shot)
            for rem in self.removeList:
                try:
                    self.shotList.remove(rem)
                    self.removeList.remove(rem)
                except: pass
        def collide(self, character,selfRect):
            for shot in self.shotList:
                for char in character:
                    if char!=False:
                        if char.Rect!=selfRect:
                            if shot[4]!="":
                                if shot[4].colliderect(char.Rect):
                                    char.perDamage+=shot[3]
                                    self.removeList.append(shot)
                for rem in self.removeList:
                    try:
                        self.shotList.remove(rem)
                        self.removeList.remove(rem)
                    except: pass

    class Fight (Character):
        frame=0
        pics=[]
        hit=False
        drawing=False
            
        def __init__ (self,damage,fsizex,fsizey,*args,**kwargs):
            Character.__init__(self, *args, **kwargs)
            self.damage=damage
            self.fsizex=fsizex
            self.fsizey=fsizey
            self.fRect=""
            self.pics=picUpload(self.pic)[1]
            
        def fighting(self,character,position,selfRect,fRight,fButton):
            keys=key.get_pressed()
            if self.frame>=len(self.pics):
                self.frame=0
                drawing=False
            if eval(fButton)==0:
                self.hit=False
            if eval(fButton) and self.hit==False:
                if self.frame==0:#this makes it only do damage after sprites finish
                    if fRight==True:
                        self.fRect=Rect(position[0]+self.sizex/2,position[1],self.fsizex,self.fsizey)
                    if fRight==False:
                        self.fRect=Rect((position[0]-self.fsizex)+self.sizex/2,position[1],self.fsizex,self.fsizey)
                    for char in character:
                        if char!=False:
                            if self.fRect.colliderect(char.Rect):
                                if char.Rect!=selfRect:
                                    char.perDamage+=self.damage
                                    pick=weightChoice(char.weightList)
                                    char.paralyze=char.paralyzeList[pick]
                                    if fRight:
                                        char.vx=char.distList[pick][0]
                                        char.vy=char.distList[pick][1]
                                    if fRight==False:
                                        char.vx=-1*(char.distList[pick][0])
                                        char.vy=char.distList[pick][1]
                    self.frame=0.6
                self.hit=True
                self.drawing=True
            if self.drawing and self.frame>0:
                if fRight==True:
                    screen.blit(self.pics[int(self.frame)],selfRect)
                if fRight==False:
                    screen.blit(transform.flip(self.pics[int(self.frame)],1,0),selfRect)
                self.frame+=0.4

    def drawScene (screen, characters, health):
        for i in range(len(health)):
            if health[i]!="":
                screen.blit(health[i],(92+(292*i),570))
                if characters[i]!=False:
                    damageWord=centuryfont.render((str(characters[i].perDamage)+"%"),True,(200,200,200))
                    screen.blit(damageWord,(192+(292*i),570))
                
    def runChar (characters, shooting, fight):
        if characters[0]!=False:
            characters[0].move("keys[K_UP]","keys[K_RIGHT]","keys[K_LEFT]")
            characters[0].damage()
            shooting[0].addShot(characters[0].position(),characters[0].fRight,"keys[K_SPACE]",characters[0].sizex)
            shooting[0].moveShot()
            shooting[0].collide(characters,characters[0].Rect)
            fight[0].fighting(characters,characters[0].position(),characters[0].Rect,characters[0].fRight,"keys[K_y]")
        if characters[1]!=False:
            characters[1].move("keys[K_w]","keys[K_d]","keys[K_a]")
            characters[1].damage()
            shooting[1].addShot(characters[1].position(),characters[1].fRight,"keys[K_x]",characters[1].sizex)
            shooting[1].moveShot()
            shooting[1].collide(characters,characters[1].Rect)
            fight[1].fighting(characters,characters[1].position(),characters[1].Rect,characters[1].fRight,"keys[K_t]")
        if characters[2]!=False:
            characters[2].move2(aiList1)
            characters[2].damage()
        if characters[3]!=False:
            pass
            
            
    def distance(x1,y1,x2,y2):
        return ((x1-x2)**2 + (y1-y2)**2)**0.5

    def weightChoice(weights):
        rand = random() * sum(weights)
        for pos, whey in enumerate(weights):
            rand -= whey
            if rand < 0:
                return pos

    def picUpload(name):
        length=[0,0,0,0,0]
        Walk,Fight,Shoot,Jump,Shot=[],[],[],[],[]
        pics=[Walk,Fight,Shoot,Jump,Shot]
        nList=["Walk","Fight","Shoot","Jump","Shot"]
        for i in range (5):
            length[i]=len(os.listdir(name+"/"+name+" "+nList[i]+"/"))
        for i in range (5):
            for j in range(length[i]):
                pics[i].append(image.load(name+"/"+name+" "+nList[i]+"/"+name+" "+nList[i]+str(j)+".png"))
        return (pics)

    def picUpload2(name):
        if name !="":
            return image.load(name+"/"+name+" Background"+"/"+name+" Background"+".png")
        if name =="":
            return ""

    def damageChoice(characters,ais):#make room for more lists later
        count=20
        count2=20
        count3=20
        for char in characters:
            if char!=False:
                if char.y>1000 or char.y<-200:
                    pos=characters.index(char)
                    char.lives-=1
                    for i in range(20):
                        count-=1
                        if count<=0:
                            char.x,char.y=600,200
                    if char.lives<=0:
                        characters[pos]=False
        for char2 in ais:
            if char2!=False:
                if char2.y>1000 or char2.y<-200:
                    pos=ais.index(char2)
                    char2.lives-=1
                    for i in range(20):
                        count2-=1
                        if count2<=0:
                            char2.x,char2.y=600,200
                    if char2.lives<=0:
                        ais[pos]=False

    def menuPicks():
        for p in charPick:
            if p=="Kirby":
                if charPick.index(p)>=2:
                    kirby=AI(240,430,.6,1,22,20,5,"Kirby")
                    if charPick.index(p)==2:
                        aiList2.append(kirby)
                    if charPick.index(p)==3:
                        aiList1.append(kirby)
                if charPick.index(p)<=1:
                    kirby=Character(240,430,.6,1,22,20,5,"Kirby")
                kirbyshot=Shot(30, 20, 10,8,"Kirby")
                kirbyfight=Fight(10,30,10,260,430,.6,1,22,20,5,"Kirby")
                charList[charPick.index(p)]=kirby#hit List
                shotList.append(kirbyshot)
                fightList.append(kirbyfight)

            if p=="Mewtwo":
                if charPick.index(p)>=2:
                    mewtwo=AI(240,430,.6,1,22,20,5,"Mewtwo")
                    if charPick.index(p)==2:
                        aiList2.append(mewtwo)
                    if charPick.index(p)==3:
                        aiList1.append(mewtwo)
                if charPick.index(p)<=1:
                    mewtwo=Character(240,430,.6,1,22,20,5,"Mewtwo")
                mewtwoshot=Shot(30, 20, 10,24,"Mewtwo")
                mewtwofight=Fight(10,30,10,260,430,.6,1,22,20,5,"Mewtwo")
                charList[charPick.index(p)]=mewtwo#hit List
                shotList.append(mewtwoshot)
                fightList.append(mewtwofight)

            if p=="Sonic":
                if charPick.index(p)>=2:
                    sonic=AI(240,430,.6,1,22,20,5,"Sonic")
                    if charPick.index(p)==2:
                        aiList2.append(sonic)
                    if charPick.index(p)==3:
                        aiList1.append(sonic)
                if charPick.index(p)<=1:
                    sonic=Character(240,430,.6,1,22,20,5,"Sonic")
                sonicshot=Shot(30, 20, 10,12,"Sonic")
                sonicfight=Fight(10,30,10,260,430,.6,1,22,20,5,"Sonic")
                charList[charPick.index(p)]=sonic#hit List
                shotList.append(sonicshot)
                fightList.append(sonicfight)

            if p=="Zabuza":
                if charPick.index(p)>=2:
                    zabuza=AI(240,430,.6,1,22,20,5,"Zabuza")
                    if charPick.index(p)==2:
                        aiList2.append(zabuza)
                    if charPick.index(p)==3:
                        aiList1.append(zabuza)
                if charPick.index(p)<=1:
                    zabuza=Character(240,430,.6,1,22,20,5,"Zabuza")
                zabuzashot=Shot(30, 20, 10,15,"Zabuza")
                zabuzafight=Fight(10,30,10,260,430,.6,1,22,20,5,"Zabuza")
                charList[charPick.index(p)]=zabuza#hit List
                shotList.append(zabuzashot)
                fightList.append(zabuzafight)

    p1health=picUpload2(p1)
    p2health=picUpload2(p2)
    p3health=picUpload2(p3)
    p4health=picUpload2(p4)

    healthList=[p1health,p2health,p3health,p4health]
         
    charList=[False,False,False,False]
    aiList1=[]
    aiList2=[]
    shotList=[]
    fightList=[]

    menuPicks()

    #While Loop---------------------------------------------
    myClock = time.Clock()
    running=True
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running=False
        keys = key.get_pressed()
        screen.blit(stage,(0,0))
        if keys[K_ESCAPE]:
            break
        drawScene(screen,charList,healthList)
        runChar(charList,shotList,fightList)
        damageChoice(charList,aiList1)
        display.flip()
        myClock.tick(60)
    display.flip()
    quit()

#------------------------------------------------------------------------------------------
    
page="start"
while page!="exit":
    if page=="start":
        page=start()
    if page=="menu":
        page=menu()
    if page=="character":
        page=character()
    if page == "Option":
        page = Option()
    if page == "Data":
        page = Data()
    if page=="maps":
        page=maps()
    if page=="game":
        page=game()
quit()
