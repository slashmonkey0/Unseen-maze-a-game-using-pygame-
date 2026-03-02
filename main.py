import pygame
wn=pygame.display.set_mode((640,640))
class maze_seeker:
    x=0
    y=0
    def draw(self,surface,x,y):
        self.x=x
        self.y=y
        pygame.draw.circle(surface,(255,0,0),(self.x,self.y),21)

    def draw_move(self,surface,dx,dy):
        self.x+=dx
        self.y+=dy
        if self.x<64 or self.x>576 or self.y<64 or self.y>576:
            return [self.x-dx,self.y-dy]
        self.draw(surface,self.x,self.y)
        return [self.x,self.y]

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

seeker= maze_seeker()
seeker.draw(wn,96,544)
newPosition=[96,544]
running=True
draw_grid(wn)
draw_destination(wn,544,96)
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                newPosition=seeker.draw_move(wn,0,-64)
                print("W pressed once")
            if event.key == pygame.K_a:
                newPosition=seeker.draw_move(wn,-64,0)
                print("A pressed once")
            if event.key == pygame.K_s:
                newPosition=seeker.draw_move(wn,0,64)
                print("S pressed once")
            if event.key == pygame.K_d:
                newPosition=seeker.draw_move(wn,64,0)
                print("D pressed once")
    wn.fill((0, 0, 0))        # Clear screen
    draw_grid(wn) # Redraw grid
    draw_destination(wn,544,96)            
    seeker.draw(wn,newPosition[0],newPosition[1])           # Redraw player
    pygame.display.update()   # Update screen



pygame.quit()
