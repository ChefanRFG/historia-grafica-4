import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1960, 960
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Novela Gráfica Undercaves")

images = {
    "img_inicial": pygame.transform.scale(pygame.image.load("0.png"), (WIDTH, HEIGHT)),
    "img_cueva": pygame.transform.scale(pygame.image.load("1.png"), (WIDTH, HEIGHT)),
    "img_prota": pygame.transform.scale(pygame.image.load("2.png"), (WIDTH, HEIGHT)),
    "img_ciudad": pygame.transform.scale(pygame.image.load("3.png"), (WIDTH, HEIGHT)),
    "img_puesto": pygame.transform.scale(pygame.image.load("4.png"), (WIDTH, HEIGHT)),
    "img_castillo": pygame.transform.scale(pygame.image.load("5.png"), (WIDTH, HEIGHT)),
    "img_monstruo_de_caballeria": pygame.transform.scale(pygame.image.load("6.png"), (WIDTH, HEIGHT)),
    "img_espada_legendaria": pygame.transform.scale(pygame.image.load("7.png"), (WIDTH, HEIGHT)),
    "img_monstruo_boss": pygame.transform.scale(pygame.image.load("8.png"), (WIDTH, HEIGHT)),
    "img_monstruo_boss_2": pygame.transform.scale(pygame.image.load("10.png"), (WIDTH, HEIGHT)),
    "img_boss_caballero_monstruo": pygame.transform.scale(pygame.image.load("11.png"), (WIDTH, HEIGHT)),
    "img_los_caballeros_del_destino": pygame.transform.scale(pygame.image.load("12.png"), (WIDTH, HEIGHT)),
    "img_boss_final_caballero_obscuro": pygame.transform.scale(pygame.image.load("13.png"), (WIDTH, HEIGHT)),
    "img_campo_de_batalla_final": pygame.transform.scale(pygame.image.load("14.png"), (WIDTH, HEIGHT))
}

# Fuente de texto
font = pygame.font.Font(None, 36)

def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

class GameState:
    def __init__(self):
        self.state = "Iniciar el Crono"
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.handle_key_1()
            elif event.key == pygame.K_2:
                self.handle_key_2()
    
    def handle_key_1(self):
        if self.state == "Iniciar el Crono":
            self.state = "buscar una salida"
        elif self.state == "buscar una salida":
            self.state = "Rendirte ante el frio"
        elif self.state == "Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)":
            self.state = "Ir hacia la luz"
        elif self.state == "Rendirte ante el frio":
            self.state = "Moriste congelado"
        elif self.state == "Ir hacia la luz":
            self.state = "Ir a comer algo al puesto de comida"
        elif self.state == "Ir a comer algo al puesto de comida":
            self.state = "Fuiste a comer al puesto de comida, eventualmente te sentiste mal y explotaste."
        elif self.state == "Ir hacia el castillo a investigar sobre el pueblo":
            self.state = "Hablar con el monstruo"
        elif self.state == "Hablar con el monstruo":
            self.state = ""



        
    
    def handle_key_2(self):
        if self.state == "Iniciar el Crono":
            self.state = "Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)"
        elif self.state == "buscar una salida":
            self.state = "Seguir buscando una salida"
        elif self.state == "Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)":
            self.state = "Retroceder para buscar la salida"
        elif self.state == "Ir hacia la luz":
            self.state = "Ir hacia el castillo a investigar sobre el pueblo"
        elif self.state == "Ir hacia el castillo a investigar sobre el pueblo":
            self.state = "Intentar pelear con el con tus habilidades magicas"
        elif self.state == "":
            self.state = ""
        elif self.state == "":
            self.state = ""


    def show(self):
        screen.fill(BLACK)
        if self.state == "Iniciar el Crono":
            screen.blit(images["img_inicial"], (0, 0))
            draw_text("Caiste de una altura muy alta, estas conmocionado y parece que estas herido internamente", 30, 300)
            draw_text("Recuerdas quien eres de golpe, Zhongli, exacto, eres el heroe legendario de la superficie", 30, 330)
            draw_text("Zhongli: claro, ahora lo rexcuerdo, estaba de expedicion cuando una brecha de portal me absorbio al sub-suelo, es bastante diferente a las leyendas...", 30, 360)
            draw_text("Zhongli: Bueno, *ahhhh* sera mejor que comience a caminar por aca, hace bastante frio a decir verdad...", 30, 390)
            draw_text("Opciones del destino", 50, 500)
            draw_text("1. Buscar una salida", 50, 550)
            draw_text("2. Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)", 50, 600)
        elif self.state == "buscar una salida":
            screen.blit(images["img_cueva"], (0, 0))
            draw_text("Te perdiste buscando la salida, sientes el frio comenzando a afectarte poco a poco...", 50, 100)
            draw_text("1. Rendirte ante el frio", 50, 150)
            draw_text("2. Seguir buscando una salida", 50, 200)
        elif self.state == "Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)":
            screen.blit(images["img_cueva"], (0, 0))
            draw_text("Ves una luz al final de el tunel, deseas ir hacia ella?", 50, 100)
            draw_text("1. Ir hacia la luz", 50, 150)
            draw_text("2. Retroceder para buscar la salida", 50, 200)
        elif self.state == "Rendirte ante el frio":
            draw_text("Moriste congelado", 50, 50)
        elif self.state == "Ir hacia la luz":
            screen.blit(images["img_ciudad"], (0, 0))
            draw_text("Caes encima de la ciudad, es enorme y repleta de monstruos como personas, ves un puesto de comida a lo lejos y un castillo algo tetrico", 50, 100)
            draw_text("1. Ir a comer algo al puesto de comida", 50, 100)
            draw_text("2. Ir hacia el castillo a investigar sobre el pueblo",50, 100)
        elif self.state == "Ir a comer algo al puesto de comida":
            screen.blit(images["img_puesto"], (0, 0))
            draw_text("Fuiste a comer al puesto de comida, eventualmente te sentiste mal y explotaste.", 50, 100)
        elif self.state == "Ir hacia el castillo a investigar sobre el pueblo":
            screen.blit(images["img_castillo"], (0, 0))
            draw_text("Fuiste al castillo y en la puerta habia un gigante monstruoso, parecia ser el portero de este", 50, 100)
            draw_text("1. Hablar con el monstruo", 50, 150)
            draw_text("2. Intentar pelear con el con tus habilidades magicas", 50, 200)
        elif self.state == "Hablar con el monstruo":
            draw_text("Te acercas para hablar con el monstruo, en tu platica te habla del reino Puertero: Este reino se formo hace /'¿*0'¿/0' *ilegible* años, todo era pascifico hasta que el vasio se apodero de las fonteras del reino", 50, 100)
            draw_text("Segun la profecia un guerrero de aura carmesi nos librara de este fatidico final, y tal parece que ese eres tu.", 50, 150)
            draw_text("Zhongli: YO!? De que hablas? soy un heroe de la superficie no de las catacumbas del sub-suelo", 50, 200)
        elif self.state == "":
            draw_text("", 50, 50)
        elif self.state == "":
            screen.blit(images[""], (0, 0))
            draw_text("", 50, 100)
        elif self.state == "":
            draw_text("", 50, 50)
            
        pygame.display.update()

def game():
    game_state = GameState()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            game_state.handle_event(event)
        
        game_state.show()
        pygame.display.flip()

game()