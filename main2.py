from pygame import*
from random import*
from math import*
import os

#Make AI shoot and fight
#do the drawing in separate function outside

screen=display.set_mode((1260,700))
stage=image.load("space-background.png")
##stage=transform.scale(stage,(1260,700))

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
    frame=0 #put inside function

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
        #fix the physics for when both right and left buttons are pressed
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
            self.vy=-13 #used to be 10
            self.numofjump-=1
            self.onGround=False
            self.kup=False
            
        self.vy+=0.8*self.weight#was multiplied by 0.5 before
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

class AI(Character): #also make a better pririty 
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
    def __init__(self, speed, sizex, sizey, pic):
        self.speed=speed
        self.sizex=sizex
        self.sizey=sizey
        self.shotRect=""
        self.shotList=[]
        self.count=0
        self.pic=pic
        self.pics=picUpload(self.pic)[4]
    def addShot(self,position,fRight,damage,sButton,size):
        keys=key.get_pressed()
        if eval(sButton)==0:
            self.shotKey=True
        if eval(sButton) and self.shotKey==True and self.count==0:
            if fRight==True:
                self.shotList.append([position[0]+size+1,position[1],True,damage,self.shotRect])
            if fRight==False:
                self.shotList.append([position[0]-self.sizex-1,position[1],False,damage,self.shotRect])
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
##            shot[4]=Rect(shot[0],shot[1]-self.sizey,self.sizex*2,self.sizey*2)
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

#make everything drawn here and NOT inside classes
def drawScene (screen, characters, health):
    for i in range(len(health)):
        screen.blit(health[i],(92+(292*i),570))
        if characters[i]!=False:
            damageWord=centuryfont.render((str(characters[i].perDamage)+"%"),True,(200,200,200))
            screen.blit(damageWord,(192+(292*i),570))
            
#ADDSHOT is HERE
def runChar (characters, shooting):
    if characters[0]!=False:
        characters[0].move("keys[K_UP]","keys[K_RIGHT]","keys[K_LEFT]")
        characters[0].damage()
        shooting[0].addShot(characters[0].position(),characters[0].fRight,8,"keys[K_SPACE]",characters[0].sizex)
        shooting[0].moveShot()
        shooting[0].collide(characters,characters[0].Rect)
    if characters[1]!=False:
        characters[1].move("keys[K_w]","keys[K_d]","keys[K_a]")
        characters[1].damage()
        shooting[1].addShot(characters[1].position(),characters[1].fRight,12,"keys[K_x]",characters[1].sizex)
        shooting[1].moveShot()
        shooting[1].collide(characters,characters[1].Rect)
    if characters[2]!=False:
        characters[2].move2(aiList1)
        characters[2].damage()
        
        
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
    return image.load(name+"/"+name+" Background"+"/"+name+" Background"+".png")

def damageChoice(characters,ais):#make room for more lists later
    for char in characters:
        if char!=False:
            if char.y>1000 or char.y<-200:
                pos=characters.index(char)
                characters[pos]=False
    for char2 in ais:
        if char2!=False:
            if char2.y>1000 or char2.y<-200:
                pos=ais.index(char2)
                ais[pos]=False

def menuPicks():
    pass


p1health=picUpload2("Kirby")
p2health=picUpload2("Sonic")
p3health=picUpload2("Zabuza")
##p4health=picUpload2("Kirby Background")

healthList=[p1health,p2health,p3health]
    
#Characters---------------------------------------------
kirby=Character(240,430,.6,1,22,20,5,"Kirby")
kirbyshot=Shot(30, 20, 10,"Kirby")
kirbyfight=Fight(10,30,10,260,430,.6,1,22,20,5,"Kirby")

sonic=Character(500,430,.6,1,22,20,5,"Sonic")
sonicshot=Shot(20,50,20,"Sonic")
sonicfight=Fight(20,30,10,500,430,.6,1,22,20,5,"Sonic")

whatever=AI(600,430,.6,1,34,50,5,"Zabuza")
     
charList=[]
aiList1=[]
shotList=[]
fightList=[]
picList=[]
#platList=[]

charList.extend([kirby,sonic,whatever])#hit list
aiList1.extend([kirby,sonic])#follow list, so another list for another ai
shotList.extend([kirbyshot,sonicshot])#shot type list

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
    runChar(charList,shotList)
    damageChoice(charList,aiList1)
    kirbyfight.fighting(charList,kirby.position(),kirby.Rect,kirby.fRight,"keys[K_y]")
    sonicfight.fighting(charList,sonic.position(),sonic.Rect,sonic.fRight,"keys[K_t]")
    drawScene(screen,charList,healthList)
    display.flip()
    myClock.tick(60)
quit()
