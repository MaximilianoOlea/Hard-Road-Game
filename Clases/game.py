import pygame

import sys 

from Configuraciones.config_assets import *

from Configuraciones.mode import *

from Configuraciones.diccionarios_assets import *

from .object_game import Object_game

from .character import Character

from .character_main import Pingu

from .item import *

from .enemy import Enemy
class Game:
    def __init__(self, size_screen: tuple, name_game: str,icon_path:str):

        pygame.init()
        self.screen = pygame.display.set_mode((size_screen))
        pygame.display.set_caption(name_game)
        self.clock = pygame.time.Clock()
        icon = pygame.image.load (icon_path)
        pygame.display.set_icon(icon)
        
        # Estado del juego
        self.playing = False
        self.finished = True
        self.pause = False
        # ----------------------------------------------------

        #Test:
        self.background = pygame.image.load("assets\\backgrounds\grass.png").convert()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))
        
        #Sprites
        self.all_sprites = pygame.sprite.Group()
        self.pingu = Pingu()
        self.projectiles_pingu = pygame.sprite.Group()#Se crean cuando dispara
        self.all_sprites.add(self.pingu)

        #Piso
        self.piso = pygame.Rect(0,0,WIDTH,20)
        # self.piso.top = self.pingu.sides["main"].bottom
        self.piso.top= self.pingu.sides["main"].bottom
        self.lados_piso = get_rectangles(self.piso)

        #Main character




# Estados del juego


    def start(self, fps: int):
        """_summary_
            Comienza el juego
        Args:
            fps (int): Velocidad en la que correrá el juego
        """
        self.playing = True
        self.finished = False

        while self.playing:
            self.clock.tick(fps)
            self.handle_event(self.background,self.lados_piso)
    def exit(self):
        """Salir definitivamente del juego
        """
        pygame.quit()
        sys.exit()

    def finished_game(self):
        """Terminar la partida pero no salir del juego
        """
        self.jugando = False
        self.finished = True

    def game_over(self):
        """Termina la partida pero no el juego
        """
        self.finalizado = True
        self.show_screen_game_over()

# -------------------

    def reset(self):  # Debe recibir el nivel
        pass

    # Muestra la pantalla de partida perdida
    def show_screen_game_over(self, image):
        pass

    def show_screen_pause(self):
        # Pausa el juego,muestra Opcion de Reinicio | volver al juego |Salir al menu principal
        self.pause = not self.pause
        self.play_sound(rf"assets\sounds\menu\pause.mp3")
        return self.pause
#Manejador de eventos:
    def handle_event(self,background,floor):
        """_summary_
        Controla los eventos del juego
        """
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.exit()

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    change_mode()  # Modo admid (Ver rectangulos de colision)
                elif evento.key == pygame.K_RETURN:
                    self.show_screen_pause()
                elif evento.key == pygame.K_j or evento.key == pygame.K_z:
                    if not self.pause:
                        self.pingu.is_doing = "dispara"              
                        self.pingu.shoot_projectile_pingu(
                        rf"assets\sounds\pingu\proyectile.mp3",self.pingu.sides["main"][0],self.pingu.sides["main"][1],
                        self.pingu.is_looking,self.projectiles_pingu,self.all_sprites) 

        if not self.pause:
            self.controller_movement()
            self.render_screen(background,floor)
            #Si cae sobre un enemigo



#------------------------------------------------------

    def render_screen(self, background,floor):#Object_game seran una lista
        """_summary_
        Actualiza los elementos de la pantalla

        Args:
            screen (_type_): Pantalla en la que va a blitearse
            object_game (list): Todos los elementos del juego (Lista de diccionarios)
        """

        self.screen.blit(background,(ORIGIN))   

        if not self.pause:
            if len(self.projectiles_pingu)>0:
                for projectile in self.projectiles_pingu:
                    projectile.draw(self.screen)
                    projectile.update()
                    projectile.draw_rectangles(self.screen,"Orange",3)
            # self.pingu.update()
            # self.pingu.draw(self.screen)
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            self.pingu.check_collision_floor(floor)

        
        #MODO ADMIN:
        self.pingu.draw_rectangles(self.screen,"Green",3)
        if get_mode():
            for lado in self.lados_piso:
                pygame.draw.rect(self.screen,"Yellow",self.lados_piso[lado],3)

        pygame.display.flip()


#---------------------------------------------------------
    def add_sprite(self,element_sprite):

        self.sprites.add(element_sprite)


    def play_sound (self,sound):
        pygame.mixer.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()

    def play_music (self,sound):
        pygame.mixer.init
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(-1)

    def controller_movement (self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.pingu.is_doing = "izquierda"
            self.pingu.is_looking = "izquierda"

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.pingu.is_doing = "derecha"
            self.pingu.is_looking = "derecha"
        elif keys[pygame.K_x] or keys[pygame.K_k]:
            self.pingu.is_doing = "salta"
        elif keys[pygame.K_j] or keys[pygame.K_z]:
            self.pingu.is_doing = "dispara"              
        else:
            self.pingu.is_doing = "quieto"      