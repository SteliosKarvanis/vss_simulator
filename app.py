import pygame
from pygame.event import Event
from GUI.menu import Menu
from GUI.button import Button
from simulation import Simulation
from GUI.start_menu import Start_Menu 


class App:
    def __init__(self):
        self._running = True
        self._screen = None
        self.menu = Menu()
        self.background_image = pygame.image.load("resources/background.jpeg")
        self.lawn = pygame.image.load("resources/lawn.jpeg")
        self.__update_assets__()
        self.simulation = Simulation(self.menu.configs, self.lawn)
        self.button = Button()
        self.game_state="start" #or simulation

    def on_init(self):
        pygame.init()
        self.text_font1=pygame.font.SysFont(None, 70)
        self.text_font2=pygame.font.SysFont(None, 50)
        self.start_menu=Start_Menu()
        self._screen = pygame.display.set_mode(self.menu.get_config("screen_res"))
        self._running = True

    def on_event(self, event: Event):
        if self.game_state=="start" and event.type==pygame.KEYDOWN:
            self.game_state="simulation"
        elif event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        if self._running:
            if self.game_state=="simulation":
                self.simulation.update()

    def on_render(self):
        # Draw background
        self.__update_assets__()
        #self._screen.blit(self.background_image, (0, 0))
        #self._screen.blit(self.lawn, (0, self.menu.get_config("status_bar_height")))

        if self._running:
            self._screen = self.button.draw(self._screen)
            if self.game_state=="simulation":
                self._screen.blit(self.background_image, (0, 0))
                self._screen.blit(self.lawn, (0, self.menu.get_config("status_bar_height")))
                self._screen = self.simulation.draw(self._screen)
            else:
                self._screen = self.start_menu.screen
                text1=self.text_font1.render(self.start_menu.text1,True,self.start_menu.text_color)
                text2=self.text_font2.render(self.start_menu.text2,True,self.start_menu.text_color)
                text3=self.text_font2.render(self.start_menu.text3,True,self.start_menu.text_color)
                text4=self.text_font2.render(self.start_menu.text4,True,self.start_menu.text_color)
                self._screen.blit(text1,(0,self.start_menu.height/4))
                self._screen.blit(text3,(0,self.start_menu.height/2))
                self._screen.blit(text4,(0,self.start_menu.height/2+50))
                self._screen.blit(text2,(0,self.start_menu.height*2/3))
        else:
            pass
        # Update the display
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def __update_assets__(self):
        self.background_image = pygame.transform.scale(
            self.background_image, (self.menu.get_config("screen_res")[0], self.menu.get_config("status_bar_height"))
        )
        self.lawn = pygame.transform.scale(self.lawn, self.menu.get_config("field_size"))
