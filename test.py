import pygame

class player:
    def __init__(self):
        self.money=0
        self.earn=1
        self.member={}
        self.image=pygame.image.load("character.jpg")

def rungame():
    button1=pygame.image.load("button_whoweare.png")
    TARGET_FPS=30
    clock=pygame.time.Clock()
    p=player()
    flag=False
    time=90
    background=pygame.image.load("back.jpg")
    while True:
        screen.fill((255,255,255))
        time-=1
        #끄기
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)



        #배경과 캐릭터
        screen.blit(background,(0,0))

        pRectobj=p.image.get_rect()
        pRectobj.center=(320,240)
        screen.blit(p.image, pRectobj)

        screen.blit(button1, (10, 400))

        fontObj=pygame.font.Font(None,60)
        textSurfaceObj=fontObj.render(str(p.money),True,(60,60,0))
        textRectObj=textSurfaceObj.get_rect()
        textRectObj.center=(600,50)
        screen.blit(textSurfaceObj,textRectObj)

        LEFT=1
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==LEFT:
            flag=True

        if flag and event.type==pygame.MOUSEBUTTONUP and event.button==LEFT:
            pos=pygame.mouse.get_pos()
            x=p.image.get_width()
            y=p.image.get_height()
            if pos[0]>320-x/2 and pos[0]<320+x and pos[1]>240-y and pos[1]<240+y:
                p.money+=p.earn
            flag=False
            time=90

        elif time==0:
            fontObj = pygame.font.Font(None, 23)
            textSurfaceObj = fontObj.render('Give Money!', True, (0, 0, 0))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (280, 180)
            screen.blit(textSurfaceObj, textRectObj)
            time+=1

        clock.tick(TARGET_FPS)
        pygame.display.flip()




pygame.init()

width, height=640, 480

screen=pygame.display.set_mode((width,height))

rungame()