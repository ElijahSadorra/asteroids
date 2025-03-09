import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill("black")

        pygame.display.flip()


    pygame.quit()



if __name__ == "__main__":
    main()
