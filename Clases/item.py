import pygame

from .object_game import Object_game

from .character import Character

from Configuraciones.config_assets import WIDTH

class Item(Object_game):
    def __init__(self, animations: list, key_animation: str, size_character: tuple, initial_position:tuple):
        super().__init__(
            animations, key_animation, size_character, initial_position)
            

    def aplicar_efecto (self, unPersonaje:Character):
        pass


class Projectile (Item):
    def __init__(self, animations: list, key_animation: str, size_projectile: tuple, initial_position:tuple,speed_proyectile,direction_projectile:str):
        super().__init__(
            animations, key_animation, size_projectile, initial_position)  
        self.speed = speed_proyectile

        self.direction_projectile = direction_projectile
        self.collide = False


    def trajectory (self):
        pass

    def draw(self,screen):
        self.animate_motion(screen,"derecha")

    def check_objective (self,a_objective:Character):
        
        for side in self.sides:
            if self.sides[side].colliderect(a_objective.sides["main"]) and not self.collide :
                self.kill()
                self.play_sound("assets\sounds\pingu\proyectile_collide.mp3")
                a_objective.count_life -= 1
                print (a_objective.count_life)
                if (a_objective.count_life < 1):
                    a_objective.kill()
                self.collide = True

    def update(self):
        if self.direction_projectile == "derecha":
            self.move(self.speed)
        elif self.direction_projectile == "izquierda":
            self.move(self.speed*-1)

        if self.sides["main"].left <= 0 or self.sides["main"].right >= WIDTH:
            self.kill()
            self.play_sound("assets\sounds\pingu\proyectile_collide.mp3")