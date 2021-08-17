import pygame
import random
import animation

#classe qui gère la notion de monstre
class Monster(animation.animateSprite):

    def __init__(self, game) -> None:
        super().__init__("mummy")
        self.attack = 1
        self.max_health = 100
        self.health = self.max_health
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 540
        self.velocity = 0.4 + random.randint(0,3) / 10 
        self.game = game
        self.start_animation()

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            # reaparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0,300)
            self.health = self.max_health
            self.velocity = 0.4 + random.randint(0, 3) / 10

        # si la barre d'evenenement est a son maximum
        if self.game.comet_event.is_full_loaded() :
            # On retire su jeu le monstre
            self.game.all_monsters.remove(self)
            self.game.comet_event.attempt_fall()

    def update_animation(self) :
        self.animate(loop=True)

    def update_health_bar(self, surface):
        pygame.draw.rect(surface,(60,63,60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])
        

    def forward(self):
        # le deplacmeent ne se fait que lors qu'il n y a pas de collition avec un joueur
        if not(self.game.check_collision(self, self.game.all_players)):
            self.rect.x -= self.velocity
        else: 
            self.game.player.damage(self.attack)

    
