from sounds import soundManager
import pygame
from player import Player
from monster import Alien, Monster, Mummy
from comet_event import CometFallEvent
from sounds  import soundManager

# class jeu
class Game :
    def __init__(self) -> None:
        self.is_playing = False
        # chargement du joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evenenemt de commete
        self.comet_event = CometFallEvent(self)

        # groupe de Monstre
        self.all_monsters = pygame.sprite.Group()
        self.score = 0
        self.font = pygame.font.Font("assets/my_custom_font.ttf", 25)
        self.pressed = {}   
        self.sound_manager = soundManager()
        
    def start(self):
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
        self.is_playing = True
        self.player.health = self.player.max_health 
        self.pressed = {}        
        
    def add_score(self, score = 10):
        self.score += score
    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.is_playing = False
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.all_projectiles = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.score = 0
        self.sound_manager.play('game_over')

    def update(self, screen):
        # afficher le score sur l'écran
        score_text = self.font.render(f"score : {self.score}", 1, (0,0,0))
        screen.blit(score_text, (20, 20))

        screen.blit(self.player.image, self.player.rect)

        # actualisé la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser l annimation du joueur
        self.player.update_animation()

        # actualisé la barre d evenement du jeu
        self.comet_event.update_bar(screen)

        # recupérer les projectile du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()
            projectile.update_animation()


        # gestion des projectiles
        self.player.all_projectiles.draw(screen)

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        self.all_monsters.draw(screen)

        # ensemble des image de mon groupe des commete
        self.comet_event.all_comets.draw(screen)

        for comet in self.comet_event.all_comets:
            comet.fall()
            

        #gestion des touche
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x  + self.player.rect.width < screen.get_width()  :
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def check_collision(self, sprite, group):
        return(pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask))

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))


        
