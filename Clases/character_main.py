import pygame

import time 

from .character import Character

from .item import *

from Configuraciones.diccionarios_assets import *

from Configuraciones.config_assets import *


class Pingu(Character):
    def __init__(self):
        super().__init__(
        diccionario_animaciones_pingu,"quieto",SIZE_MAIN_CHARACTER,(main_character_x,main_character_y),COUNT_LIFE_PINGU,
        JUMP_POWER_MAIN_CHARACTER,SPEED_MAIN_CHARACTER,JUMP_POWER_MAIN_CHARACTER,"derecha",GRAVITY_MAIN_CHARACTER)

        #Construccion:
        self.score = 0
        self.count_life = 1
        self.count_jump = 2
        self.count_projectile = 5
        self.is_alive = True
        self.limit_jumps = 1

        self.last_shot_time = 0
        self.time_reload = 1
        self.count_steps = 0
        
    def check_collision_enemy(self,enemies,pos_impact):
        if  self.sides["bottom"].colliderect(enemies.sides["top"]):
            enemies.kill()
            self.count_jump =+ 1
            self.is_jumping = False

    def update(self):
        match self.is_doing:
            case "derecha":
                self.is_looking = "derecha"
                self.move(self.speed)
            case "izquierda":
                self.is_looking = "izquierda"
                self.move(self.speed*-1)
            case "salta":
                if not self.is_jumping:
                    self.is_jumping = True
                    self.move(self.jump_power*-1, False)
        self.jump()

    def draw(self,screen):
        match self.is_doing:
            case "derecha":
                self.is_looking = "derecha"
                if not self.is_jumping:
                    self.animate_motion(
                        screen, "camina_derecha")
            case "izquierda":
                self.is_looking = "izquierda"
                if not self.is_jumping:
                    self.animate_motion(
                        screen, "camina_izquierda")
            case "salta":
                if not self.is_jumping:
                    self.is_jumping = True
            case "quieto":
                if not self.is_jumping:
                    if self.is_looking == "derecha":
                        self.animate_motion(screen, "quieto")
                    elif self.is_looking == "izquierda":
                        self.animate_motion(
                            screen, "quieto_izquierda")
            case "dispara":
                if not self.is_jumping:
                    if self.is_looking == "derecha":
                        self.animate_motion(screen, "dispara")
                    elif self.is_looking == "izquierda":
                        self.animate_motion(screen, "dispara_izquierda")

        self.jump_draw(screen)

    def shoot_projectile_pingu(self, sound, pos_x, pos_y,direction_projectile:str,sprites):
        current_time = time.time() # Obtener el tiempo actual en segundos
        
        # Si desde el ultimo tiro paso 1 segundo habilito a que tire de nuevo
        if current_time - self.last_shot_time >= 0.5 and self.count_projectile > 0:
            #Actualizar ultimo tiro
            self.last_shot_time = current_time  
            un_projectile = Projectile(diccionario_animaciones_projectile_pingu, "derecha", (SIZE_PROJECTILE), (pos_x, pos_y), 15,direction_projectile)
            sprites.add(un_projectile)
            self.count_projectile -= 1
            if self.count_projectile == 0:
                print ("Se acabo los tiros")
                self.count_projectile = 5
            self.play_sound(sound)

