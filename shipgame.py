import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:

    def __init__(self):
        print("initialising game")
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #game window: small screen
        self.screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))

        #game window: full screen
        """
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        """

        pygame.display.set_caption("ALIEN INVASION")

        self.ship = Ship(self)
        # self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            #self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydwon_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

        
    def _check_keydwon_events(self, event):
        # response to keypress
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
    #   elif event.key == pygame.K_SPACE:
    #       self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

        
    def _check_keyup_events(self, event):
        # response to keydown
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

        
    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        # for bullet in self.bullets.sprites():
        #   bullet.draw.bullet()
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    print("running Alien Invasion game")
    ai = AlienInvasion()
    ai.run_game()
            

        

        
