import pygame
import time

veh_list = []

# Create Vehicle Class
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]

# Create Player Class that inherits from Car Class

class Player(Vehicle):
    def motion(self):
        self.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
        self.vx = 10
        self.vy = 10

        key = pygame.key.get_pressed()

        for i in range(2):
            if key[self.move[i]]:
                self.rect.x += self.vx * [-1, 1][i]

        for i in range(2):
            if key[self.move[2:4][i]]:
                self.rect.y += self.vy * [-1, 1][i]

class Comp_vehicle(Vehicle):

    def motion(self):
        self.x += self.speed
        self.rect.center = [self.x, self.y]



def main():
    
    # Initialize game window
    width = 1200
    height = 600
    blue_color = (97, 159, 182)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    time_count = 0
    veh_list = []
    # Game initialization
    stop_game = False

    

    
    # initialize player and add direction button controls
    player = Player('images/player_image.png', 40, 50, 0)

    while not stop_game:
        for event in pygame.event.get():
            
            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        player.motion()
        veh_generate()

        for veh in veh_list:
            veh.motion()
            if veh.x < -50:
                veh_list.remove(veh)

        #hit = pygame.sprite.spritecollide(player, comp_group, True)

        #if hit:
            # if collision is detected end the game
            #stop_game = True

        # Draw background
        screen.fill(blue_color)
        #screen.blit(background_image, [0, 0])

        # Draw player, enemy, and other vehicles
        player_group = pygame.sprite.Group()
        player_group.add(player)
        player_group.draw(screen)

        computer_group = pygame.sprite.Group()
        for veh in veh_list:
            computer_group.add(veh)
        computer_group.draw(screen)





       



        # Game display
        pygame.display.update()

    pygame.quit()

def veh_generate():
    y_pos = 0
    if time_count == 0:
            #lane == randint(0,7)
        lane = 0
        if lane == 0:
            y_pos = 50
    elif time_count == 500:
        time_count = 0
    time_count += 1
    veh_list.append(Comp_vehicle('images/computer_car.png', 1400, y_pos, -5))

if __name__ == '__main__':
    main()