import pygame
import time
from .object_game import Object_game
from Configuraciones.diccionarios_assets import diccionario_movimientos


class Character(Object_game):
    def __init__(self, animations: list, key_animation: str, size_character: tuple, initial_position: tuple,count_life:int ,jump_power: int, speed: int, limit_speed_fall: int, is_looking: str, gravity: int):
        super().__init__(
            animations, key_animation, size_character, initial_position)
        
        # Movimiento
        self.speed = speed
        # Salto y caida
        self.gravity = gravity
        self.jump_power = jump_power
        self.limit_speed_fall = limit_speed_fall
        self.is_jumping = False
        self.is_in_floor = True
        self.movement_y = 0
        self.is_looking = is_looking
        self.count_life = count_life
        self.is_doing = "quieto"

    def check_collision_floor(self,floor:dict):
        """_summary_

        Args:
            floor (dict): Recibe un piso y si hay colision se iguala el bottom del objeto con el top del piso
        """

        if self.sides["bottom"].colliderect(floor["top"]):
            self.movement_y = 0
            self.is_jumping = False
            self.sides["main"].bottom = floor["main"].top


    def jump(self):
        for lado in self.sides:
            self.sides[lado].y += self.movement_y
        if self.movement_y + self.gravity < self.limit_speed_fall:
            self.movement_y += self.gravity

    def jump_draw(self,screen:pygame.Surface):
        if self.is_jumping:
            if self.is_looking == "derecha":
                self.animate_motion(screen, "salta")
            else:
                self.animate_motion(
                    screen, "salta_izquierda")

    def shoot_projectile(self,sound:str,screen:pygame.Surface):
        # def shoot_projectile (self,target,sound,projectile,speed_projectile): Elementos que tengo que recibir por parametro
        # Debo definir una clase proyectil
        reload = int(time.time())%2
        print (reload)
        if reload >= 1:
            reload = 0
            self.play_sound(sound)
        # Debo agregar el projectile a la lista de sprites y a una lista de projectiles


# Restringir movimientos:


    def _limit_moves_right(self, limit_right):
        limit = True

        if self.sides["main"].right >= limit_right:
            limit = True
        else:
            limit = False

        return limit

    def _limit_moves_left(self, limit_left):
        limit = True

        if self.sides["main"].left <= limit_left:
            limit = True
        else:
            limit = False

        return limit

    def _limit_moves_top(self, limit_top):
        limit = True

        if self.sides["main"].top <= limit_top:
            limit = True
        else:
            limit = False

        return limit

    def limit_moves(self, limit, option: str) -> bool:
        match option:
            case "derecha":
                return self._limit_moves_right(limit)
            case "izquierda":
                return self._limit_moves_left(limit)
            case "top":
                return self._limit_moves_top(limit)
            

# -------------------------------------------------------
