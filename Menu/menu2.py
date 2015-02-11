#menu
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

init () #initializes the mixer music into python pygame
mixer.music.load ("Super Smash Bros Brawl -Main Menu Theme- (In HD).mp3")  #loads and plays the music 
mixer.music.play ()

screen=display.set_mode((800,600))


menu=image.load("i27i2c.png")

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

def cursormove(cursor1,cursor2):
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
    cursor1.Rect=Rect(cursor1.x+20,cursor1.y,cursor1.x+40,cursor1.y+20)

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
        cursor2.Rect=Rect(cursor2.x+20,cursor2.y,cursor2.x+40,cursor2.y+20)
        
def menu():
    running=True
    battleRect=Rect(122,122,309,153)
    battlepic=image.load("bigbutton.png")#40 pixels bigger
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"
        
        screen.blit(mainmenu,(0,0))

        mpos=mouse.get_pos()
        mb=mouse.get_pressed()

        if battleRect.collidepoint(mpos):
            screen.blit(battlepic,(battleRect.x-20,battleRect.y-20))
            if mb[0]==1:
                return "character"
        display.flip()


def character():
    running=True
    fmario = image.load("Mario!!!!!!!!!!!!!!!!.png")
    fmario2 = transform.scale(fmario,(70,50))
    fkirby = image.load("KRTDL_Kirby_Jump.png")
    fkirby2 = transform.scale(fkirby,(70,50))
    fdiddy = image.load("Diddy_Kong(Clear).png")    
    fdiddy2 = transform.scale(fdiddy,(70,50))
    fzabuza = image.load("3524834-ap89dw.png")
    fzabuza2 = transform.scale(fzabuza,(70,50))

    smario = image.load("Mario.png")
    smario2 = transform.scale(smario,(60,60))
    skirby = image.load("Kirby_Wii.png")
    skirby2 = transform.scale(skirby,(60,60))
    sdiddy = image.load("Diddy_Kong.png")    
    sdiddy2 = transform.scale(sdiddy,(60,60))
    szabuza = image.load("zabuza.png")
    szabuza2 = transform.scale(szabuza,(60,60))
    
    charselect=image.load("brawl_roster_template_by_teh_silver_wolfeh-d4djnxm.png")
    charselect=transform.scale(charselect,(800,600))
    first=Picker(150,400)
    second=""
    cursorList.extend([first,second])
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        screen.blit(charselect,(0,0))
        keys = key.get_pressed() #makes a list of the keys on the keyboard
        
        screen.blit(fmario2,(200,150))
        screen.blit(fkirby2,(210,210))
        screen.blit(fdiddy2,(300,160))
        screen.blit(fzabuza2,(310,220))

        if 200 < cursor1.x < 270 and 150 < cursor1.y < 200 and keys[K_p] == 1:
            screen.blit(smario2,(100,325))
        elif 210 < cursor1.x < 280 and 210 < cursor1.y < 260 and keys[K_p] == 1:
            screen.blit(skirby2,(100,325))
        elif 300 < cursor1.x < 370 and 160 < cursor1.y < 210 and keys[K_p] == 1:
            screen.blit(sdiddy2,(100,325))
        elif 310 < cursor1.x < 380 and 220 < cursor1.y < 270 and keys[K_p] == 1:
            screen.blit(szabuza2,(100,325))

        if 200 < cursor2.x < 270 and 150 < cursor2.y < 200 and keys[K_p] == 1:
            screen.blit(smario2,(200,325))
        elif 210 < cursor2.x < 280 and 210 < cursor2.y < 260 and keys[K_p] == 1:
            screen.blit(skirby2,(200,325))
        elif 300 < cursor2.x < 370 and 160 < cursor2.y < 210 and keys[K_p] == 1:
            screen.blit(sdiddy2,(200,325))
        elif 310 < cursor2.x < 380 and 220 < cursor2.y < 270 and keys[K_p] == 1:
            screen.blit(szabuza,(200,325))

        if keys[K_ESCAPE]:
            return "menu"

        if keys[K_5]:#make this if selections are done
            return "maps"
        
        if keys[K_2] and second=="":  #if the second hand isn't on the screen
            #make a box light up for p2
            second=Picker(300,400)
            cursorList.append(second)
       
        cursormove(hand,first,second)
    
        display.flip()

def pickcharacter():
    if page == "character":
        running = True
        fmario = image.load("Mario!!!!!!!!!!!!!!!!.png")
        fmario2 = transform.scale(fmario,(70,50))
        fkirby = image.load("KRTDL_Kirby_Jump.png")
        fkirby2 = transform.scale(fkirby,(70,50))
        fdiddy = image.load("Diddy_Kong(Clear).png")    
        fdiddy2 = transform.scale(fdiddy,(70,50))
        fzabuza = image.load("3524834-ap89dw.png")
        fzabuza2 = transform.scale(fzabuza,(70,50))

        smario = image.load("Mario.png")
        smario2 = transform.scale(smario,(60,60))
        skirby = image.load("Kirby_Wii.png")
        skirby2 = transform.scale(skirby,(60,60))
        sdiddy = image.load("Diddy_Kong.png")    
        sdiddy2 = transform.scale(sdiddy,(60,60))
        szabuza = image.load("zabuza.png")
        szabuza2 = transform.scale(szabuza,(60,60))

        while running:
            for evnt in event.get():          
                if evnt.type == QUIT:
                    running = False
            keys = key.get_pressed()  #makes a list of the keys on the keyboard
            screen.blit(fmario2,(200,150))
            screen.blit(fkirby2,(210,210))
            screen.blit(fdiddy2,(300,160))
            screen.blit(fzabuza2,(310,220))

            if 200 < cursor1.x < 270 and 150 < cursor1.y < 200 and keys[K_p] == 1:
                screen.blit(smario2,(100,325))
            elif 210 < cursor1.x < 280 and 210 < cursor1.y < 260 and keys[K_p] == 1:
                screen.blit(skirby2,(100,325))
            elif 300 < cursor1.x < 370 and 160 < cursor1.y < 210 and keys[K_p] == 1:
                screen.blit(sdiddy2,(100,325))
            elif 310 < cursor1.x < 380 and 220 < cursor1.y < 270 and keys[K_p] == 1:
                screen.blit(szabuza2,(100,325))

            if 200 < cursor2.x < 270 and 150 < cursor2.y < 200 and keys[K_p] == 1:
                screen.blit(smario2,(200,325))
            elif 210 < cursor2.x < 280 and 210 < cursor2.y < 260 and keys[K_p] == 1:
                screen.blit(skirby2,(200,325))
            elif 300 < cursor2.x < 370 and 160 < cursor2.y < 210 and keys[K_p] == 1:
                screen.blit(sdiddy2,(200,325))
            elif 310 < cursor2.x < 380 and 220 < cursor2.y < 270 and keys[K_p] == 1:
                screen.blit(szabuza,(200,325))

            display.flip()
    

def maps():
    running=True
    mapselect=image.load("2afxw2g.png")
    mapselect=transform.scale(mapselect,(800,600))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        screen.blit(mapselect,(0,0))
        cursormove(hand, cursorList[0],cursorList[1])
        display.flip()


    
page="start"
while page!="exit":
    if page=="start":
        page=start()
    if page=="menu":
        page=menu()
    if page=="character":
        page=character()
        pickcharacter()
    if page=="maps":
        page=maps()
quit()
