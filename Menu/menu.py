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



#for pause feature:
#make nested loop---->in which there is a while loop that traps the program
#ex:
#while true:
    #        """game stuff"""
    #pauseFlag=False
    #while pauseFlag=True:
        #screen.blit(resume) <---- and exit and stuff like that
        #if click resume: break <---- use mx,my[mpos],mb.collidepoint stuff

from pygame import *
from random import *

##init () #initializes the mixer music into python pygame
##mixer.music.load ("Super Smash Bros Brawl -Main Menu Theme- (In HD).mp3")  #loads and plays the music 
##mixer.music.play ()

screen=display.set_mode((800,600))


menu=image.load("Menu1.png")

##settings=

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
    



def character():
    running=True
    fmewtwo = image.load("150_mewtwo___bw_style_by_pklucario-d5x7m50.png")
    fmewtwo = transform.scale(fmewtwo,(150,100))
##    x1 = fmario.get_width()/2
##    y1 = fmario.get_height()/2
    fkirby = image.load("KRTDL_Kirby_Jump.png")
    fkirby = transform.scale(fkirby,(150,100))
##    x2 = fkirby.get_width()/2
##    y2 = fkirby.get_height()/2
    fdiddy = image.load("Diddy_Kong.png")
    fdiddy = transform.scale(fdiddy,(150,100))
##    x3 = fdiddy.get_width()/2
##    y3 = fdiddy.get_height()/2
    fzabuza = image.load("3524834-ap89dw.png")
    fzabuza = transform.scale(fzabuza,(150,130))
##    x4 = fzabuza.get_width()/2
##    y4 = fzabuza.get_height()/2

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
    second=Picker(300,400)
    back1Rect = Rect(50,0,50,50)
    player1select = False
    player1select1 = False
    player1select2 = False
    player1select3 = False
    player2select = False
    player2select1 = False
    player2select2 = False
    player2select3 = False
    backfix = False
    characters = [smewtwo,skirby,sdiddy,szabuza]
    player3com = characters[randint(0,3)]
    cursorList.extend([first,second])  #allows for two lists to be put into on big list (2d list)
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        screen.blit(charselect,(0,0))
        keys = key.get_pressed() #makes a list of the keys on the keyboard

        x1 = hand.get_width()
        y1 = hand.get_height()
        handRect = Rect(cursorList[0].x,cursorList[0].y,x1,y1)

        x2 = hand2.get_width()
        y2 = hand2.get_height()
        hand2Rect = Rect(cursorList[1].x,cursorList[1].y,x2,y2)


        screen.blit(fmewtwo,(100,110))
        mewtwoRect = Rect(100,110,150,100)
        screen.blit(fkirby,(170,240))
        kirbyRect = Rect(170,240,150,100)
        screen.blit(fdiddy,(340,120))
        diddyRect = Rect(340,120,150,100)
        screen.blit(fzabuza,(450,230))
        zabuzaRect = Rect(450,220,150,130)

#---------------------------------------------------------------------------------

        click = keys[K_n]

        if mewtwoRect.colliderect(handRect) and click == 1:
            player1select = True
            player1select1 = False
            player1select2 = False
            player1select3 = False            
        if player1select == True:
            screen.blit(smewtwo,(80,380))
                
        elif kirbyRect.colliderect(handRect) and click == 1:
            player1select = False
            player1select1 = True
            player1select2 = False
            player1select3 = False
        if player1select1 == True:
            screen.blit(skirby,(70,385))
                
        elif diddyRect.colliderect(handRect) and click == 1:
            player1select = False
            player1select1 = False
            player1select2 = True
            player1select3 = False
        if player1select2 == True:
            screen.blit(sdiddy,(70,380))
                
        elif zabuzaRect.colliderect(handRect) and click == 1:
            player1select = False
            player1select1 = False
            player1select2 = False
            player1select3 = True
        if player1select3 == True:
            screen.blit(szabuza,(80,380))

#------------------------------------------------------------------------------------------
        click2 = keys[K_z]       #SHOULD WORK BUT CANT FIX ????
        if mewtwoRect.colliderect(hand2Rect) and click2 == 1:
            player2select = True
            player2select1 = False
            player2select2 = False
            player2select3 = False            
        if player2select == True:
            screen.blit(smewtwo,(250,380))
                
        elif kirbyRect.colliderect(hand2Rect) and click2 == 1:
            player2select = False
            player2select1 = True
            player2select2 = False
            player2select3 = False
        if player2select1 == True:
            screen.blit(skirby,(250,385))
                
        elif diddyRect.colliderect(hand2Rect) and click2 == 1:
            player2select = False
            player2select1 = False
            player2select2 = True
            player2select3 = False
        if player2select2 == True:
            screen.blit(sdiddy,(250,380))
                
        elif zabuzaRect.colliderect(hand2Rect) and click2 == 1:
            player2select = False
            player2select1 = False
            player2select2 = False
            player2select3 = True
        if player2select3 == True:
            screen.blit(szabuza,(250,380))

        screen.blit(player3com,(410,380))  #everytime the character page opens u will be fighting a different computer controlled character
        
#------------------------------------------------------------------------------------
        
        
        if back1Rect.colliderect(cursorList[0].Rect): #or back1Rect.colliderect(hand2Rect):
            backfix = True
            if backfix == True:
                screen.blit(charbackpic,(0,0))
            if click == 1:
                return "menu"

            

        if keys[K_5]:#make this if selections are done
            return "maps"
        

##            cursorList.append(second)
        
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


def maps():
    running=True
    mapselect=image.load("2afxw2g (1).png")
    mapselect=transform.scale(mapselect,(800,600))
    mapbackpic = image.load("2afxw2g (2).png")
    mapbackpic = transform.scale(mapbackpic,(800,600))
    FinalDes = image.load("10445832_658916887528543_2050382375_o.jpg")
    FinalDes = transform.scale(FinalDes,(250,130))
    SP = image.load("tCk7BSV.jpg")
    SP = transform.scale(SP,(250,130))
    Dreamland = image.load("hqdefault.jpg")
    Dreamland = transform.scale(Dreamland,(250,130))
    back2Rect = Rect(0,0,80,80)
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        keys = key.get_pressed()
        x1 = hand.get_width()
        y1 = hand.get_height()
        handRect = Rect(cursorList[0].x,cursorList[0].y,x1,y1)
        screen.blit(mapselect,(0,0))
        screen.blit(FinalDes,(330,60))
        screen.blit(SP,(330,200))
        screen.blit(Dreamland,(330,340))
        click = keys[K_n]
        if back2Rect.colliderect(handRect):
            screen.blit(mapbackpic,(0,0))
            if click == 1:
                return "character"
        cursormove(hand,cursorList[0],cursorList[1])
        display.flip()

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
quit()

