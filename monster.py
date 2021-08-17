import pygame
import random
import animation

#classe qui gère la notion de monstre
class Monster(animation.animateSprite):

    def __init__(self, game, name, size, offset = 0) -> None:
        super().__init__(name, size)
        self.attack = 1
        self.max_health = 100
        self.health = self.max_health
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 540 - offset
        self.game = game
        self.start_animation()
        self.loot_amount = 10 
    def set_speed(self, speed) :
        self.default_speed = speed
        self.velocity = random.randint(1,self.default_speed) 
        
    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            # reaparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0,300)
            self.health = self.max_health
            self.velocity = self.velocity = random.randint(1,self.default_speed) 
            self.game.add_score(self.loot_amount)

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

    
#defnir une classe pour la mummy
class Mummy(Monster):
    def __init__(self, game) -> None:
        super().__init__(game, 'mummy', (130,130))
        self.set_speed(3)
        self.set_loot_amount(20)




# definir une class pour Alien 
#defnir une classe pour la mummy
class Alien(Monster):
    def __init__(self, game) -> None:
        super().__init__(game, 'alien', (300,300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(80)
