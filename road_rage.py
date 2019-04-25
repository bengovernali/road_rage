import pygame

# Create Vehicle Class
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
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




def main():
    
    # Initialize game window
    width = 1200
    height = 600
    blue_color = (97, 159, 182)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')

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

        # Draw background
        screen.fill(blue_color)
        #screen.blit(background_image, [0, 0])

        # Draw player, enemy, and other vehicles
        player_group = pygame.sprite.Group()
        player_group.add(player)
        player_group.draw(screen)

        # Game display
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()