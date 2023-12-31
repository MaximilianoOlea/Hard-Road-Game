import pygame

import time

from tools import *

from Configuraciones.mode import get_mode

class Object_game (pygame.sprite.Sprite):
    def __init__(self, animations: list, key_animation:str, size_image: tuple, initial_position: tuple,key_is_doing):
        """_summary_

        Args:
            animations (list): Lista de animaciones 
            key_animation (str): Key de la que se obtendra la primera posicion (Para la referencia de rectangulos)
            size_image (tuple): Tamaño de las animaciones
            initial_position (tuple): Posicion en la que empezará cuando se crea
        """
        super().__init__()

        self.animations = animations
        self.speed_animation = 12
        self.key_is_doing = key_is_doing
        self.index = 0
        self.image = self.animations[key_is_doing][self.index]
        # self.image = pygame.image.load(rf"assets\pingu\camina\0.png").convert_alpha()
        # self.image = pygame.transform.scale(self.image, size_image)
        # self.rect = pygame.Rect(self.image.get_rect())
        # self.rect.x = initial_position[0]
        # self.rect.y = initial_position[1]

        # Será el rect principal
        resize_animations(self.animations, size_image)

        self.rect = pygame.Rect(self.animations[key_animation][0].get_rect())
        self.rect.x = initial_position[0]
        self.rect.y = initial_position[1]

        self.sides = get_rectangles(self.rect)
        self.count_steps = 0

    def draw_rectangles(self, screen: pygame.Surface, colour: str | tuple, size: int): #G
        """_summary_
        Dibuja todos los lados que cubren al elemento
        Args:
            screen (_type_): _description_
            colour (str | tuple): nombre o valor numerico del color
            size (int): Tamaño del dibujo de los rectangulos
        """
        if get_mode():
            for side in self.sides:
                pygame.draw.rect(screen, colour, self.sides[side], size)

    # def draw (self,screen,key_is_doing:str):
    #     self.animate_motion(screen,key_is_doing,self.speed_animation)

    def move(self, speed: int, lateral_movement: bool = True):  # 
        """_summary_
            Mueve todos los rectangulos que conforman al elemento del juego
        Args:
            speed (int): Velocidad en la que se desplaza
            lateral_movement (bool, optional): True = Se mueve de forma lateral | False = Se mueve de forma vertical
        """
        if lateral_movement:
            self.rect.x += speed
            for lado in self.sides:
                self.sides[lado].x += speed
        else:
            self.rect.y += speed
            for lado in self.sides:
                self.sides[lado].y += speed
            self.movement_y = speed

    def play_sound(self, sound):
        pygame.mixer.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()

    def animate_motion(self, screen: pygame.Surface, key_animations: str):
        """_summary_
        Blitea las animaciones de un objeto
        Args:
            screen (pygame.Surface): Pantalla en la que se muestra
            images (list): Lista de imagenes que hacen la animacion
            key_animations (str): Clave del diccionario que tiene la animacion
        """
        animations = self.animations[key_animations]

        length = len(animations)

        if self.count_steps >= length:
            self.count_steps = 0
        frame = int(time.time()*self.speed_animation) % length
        screen.blit(animations[frame], self.sides["main"])
        self.count_steps += 1

