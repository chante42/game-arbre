from monster import Alien, Mummy
import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event) -> None:
        super().__init__()

        # definir l'image de cette comet
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,3)
        self.rect.x = random.randint(20,800)
        self.rect.y = -random.randint(0,800 )
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        #verifier si le nb de comet = 0
        if (len(self.comet_event.all_comets) == 0) :
            print ('evenement finis')
            self.comet_event.reset_percent()
            self.comet_event.game.start()
            
    def fall(self):
        self.rect.y += self.velocity

        # elle tombe sur le sol
        if self.rect.y >= 500:
            self.remove()

            # s'il n y a plus de boule de feu sur le jeu
            if len(self.comet_event.all_comets) == 0:
                print("l evenement est fini")
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # la boule de feu touche le sol
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ) :
            print("joueur touché !!!")
            self.remove()
            # subir des dégas
            self.comet_event.game.player.damage(20)