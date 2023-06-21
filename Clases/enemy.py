import pygame

import time 

from .character import Character

from .item import *

from Configuraciones.diccionarios_assets import *

from Configuraciones.config_assets import *

class Enemy(Character):
    def __init__(self, animations: dict, key_animation: str, size_character: 
                tuple, initial_position: tuple, jump_power: int, speed_character: int, 
                limit_speed_fall: int,is_looking:str,gravity:int,count_life:int,what_enemy:str):
        
        super().__init__(
        animations,key_animation, size_character, initial_position,jump_power,speed_character,limit_speed_fall,is_looking,gravity)

        self.count_life = count_life
        self.is_alive = True

        self.last_shot_time = 0
        self.time_reload = 10
        self.what_enemy = what_enemy
    
    def update(self):
        if self.is_looking == "derecha":
            if self.sides["main"].right <= WIDTH: #Debe recibir la plataforma
                self.move(self.speed)
            else:
                self.is_looking = "izquierda"
        elif self.is_looking == "izquierda":
            if self.sides["main"].left >= 0:
                self.move(self.speed*-1)
            else:
                self.is_looking = "derecha"

    def draw(self,screen):
        if self.is_looking == "derecha":
            self.animate_motion(screen,"camina_derecha",SPEED_ANIMATION) 
        elif self.is_looking == "izquierda":
            self.animate_motion(screen,"camina_izquierda",SPEED_ANIMATION)

    def conduct(self):
        pass

    def conduct_wolf (self):
        pass