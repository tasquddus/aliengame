import pygame

class Ship:

    def __init__(self, ai_game):
        print("getting screen")
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        print("getting rectangle")
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #starting ship at the center of the screen
        self.rect.center = self.screen_rect.center

        #storing float for ship's exact horizontal,vertical positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right, self.moving_left = False, False
        self.moving_up, self.moving_down = False, False

    def update(self):
        #updating ships x value - not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #updating y value for ship - not rect
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

