import pygame
wn=pygame.display.set_mode((640,640))
class maze_seeker:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def draw(self,surface):
        pygame.draw.circle(surface,(255,0,0),(self.x,self.y),21)
    
    def move(self,dx,dy):
        if dx>576 or dx<64:
            return 
        if dy>576 or dy<64:
            return
        self.x+=dx
        self.y+=dy
    
def draw_grid(surface):
    start_x=64
    start_y=64
    end_x=576
    end_y=64

    for i in range(9):
       pygame.draw.line(surface,(255,255,255),(start_x,start_y),(end_x,end_y),2)
       start_y+=64
       end_y+=64
    start_x=64
    start_y=64
    end_x=64
    end_y=576   
    for i in range(9):
        pygame.draw.line(surface,(255,255,255),(start_x,start_y),(end_x,end_y),2)
        start_x+=64
        end_x+=64
def draw_destination(surface,x,y):
    pygame.draw.circle(surface,(0,255,0),(x,y),21)

seeker= maze_seeker(96,544)
seeker.draw(wn)

running=True
draw_grid(wn)
draw_destination(wn,544,96)
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False



pygame.quit()