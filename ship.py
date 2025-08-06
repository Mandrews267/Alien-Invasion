import pygame 
'''Adjustments to code to resolve collision issue:'''
'''Imported Sprite in ship.py from pygame.'''
'''Added an argument to the ship class (Sprite)'''
from pygame.sprite import Sprite 



class Ship(Sprite): # inherit from sprite - may need to remove
    #A class to manage the ship.

    def __init__(self, ai_game):
        #Initialize the ship  and set its starting position.
        super().__init__() # CAll sprite initalizer - may need to remove.
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        #Store a float for the ship's exact horzontal position.
        self.x = float(self.rect.x)
        #Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #Update the ship's position baased on the movement flag.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            #self.rect.x += 1            
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            #self.rect.x -= 1
            
            #Update the rect object from self.x
        self.rect.x = int(self.x)

    def blitme(self):
        #Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        #Center the ship on the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)