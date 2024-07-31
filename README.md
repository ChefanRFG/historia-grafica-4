import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1960, 960
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Novela Gráfica Undercaves")

def load_image(name):
    try:
        return pygame.transform.scale(pygame.image.load(name), (WIDTH, HEIGHT))
    except pygame.error as e:
        print(f"Error al cargar la imagen {name}: {e}")
        return None

images = {name: load_image(f"{i}.png") for i, name in enumerate([
    "img_inicial", "img_cueva", "img_prota", "img_ciudad", "img_puesto",
    "img_castillo", "img_monstruo_de_caballeria", "img_espada_legendaria",
    "img_monstruo_boss", "img_monstruo_boss_2", "img_boss_caballero_monstruo",
    "img_los_caballeros_del_destino", "img_boss_final_caballero_obscuro",
    "img_campo_de_batalla_final"
])}

font = pygame.font.Font(None, 30)

def draw_text(text, x, y):
    screen.blit(font.render(text, True, WHITE), (x, y))

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
        transitions = {
            "Iniciar el Crono": "buscar una salida",
            "buscar una salida": "Rendirte ante el frio",
            "Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)": "Ir hacia la luz",
            "Rendirte ante el frio": "Moriste congelado",
            "Ir hacia la luz": "Ir a comer algo al puesto de comida",
            "Ir a comer algo al puesto de comida": "Fuiste a comer al puesto de comida, eventualmente te sentiste mal y explotaste.",
            "Ir hacia el castillo a investigar sobre el pueblo": "Hablar con el monstruo",
            "Hablar con el monstruo": "Ayudar con la profesia",
            "Ayudar con la profesia": "Ir hacia el rey",
            "Ir hacia el rey": "Continuar tu camino",
            "Continuar tu camino": "Esperar al rey",
            "Esperar al rey": "Ayudar a eliminar la corrupción",
            "Ayudar a eliminar la corrupción": "Ir a cumplir tu mision...",
            "Ir a cumplir tu mision...": "Proclamarse vicrtorioso...",
            "Proclamarse vicrtorioso...": "Legendary Ending. Victoria...",
            "Retroceder para buscar la salida": "Aceptar su invitacion",
            "Aceptar su invitacion": "Sientes como se consume tu alma, el caballero se hace mas poderoso..."
        }
        self.state = transitions.get(self.state, self.state)

    def handle_key_2(self):
        transitions = {
            "Iniciar el Crono": "Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)",
            "buscar una salida": "Seguir buscando una salida",
            "Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)": "Retroceder para buscar la salida",
            "Ir hacia la luz": "Ir hacia el castillo a investigar sobre el pueblo",
            "Ir hacia el castillo a investigar sobre el pueblo": "Intentar pelear con el con tus habilidades mágicas",
            "Intentar pelear con el con tus habilidades mágicas": "El monstruo acabó contigo en tan solo un movimiento de brazo, patético",
            "Hablar con el monstruo": "Irse del lugar",
            "Irse del lugar": "Decides irte sin embargo el monstruo te ataca con su arma atravesándote",
            "Esperar al rey": "Negarse ya que no tienes nada que ver con ese reino",
            "Negarse ya que no tienes nada que ver con ese reino": "Al escuchar esto el rey le ordena a tu guardia de tu ejecucion",
            "Seguir buscando una salida": "A pesar de tu desespere de buscar la salida te perdiste en el vacio de la fronteras",
            "Retroceder para buscar la salida": "Caballero desconocido: hey, que haces aca pequeño humano?",
            "Caballero desconocido: hey, que haces aca pequeño humano?": "Rechazar su oferta",
            "Rechazar su oferta": "Ah, es una lastima, total iba a consumir tu alma..."
        }
        self.state = transitions.get(self.state, self.state)

    def show(self):
        screen.fill(BLACK)
        state_texts = {
            "Iniciar el Crono": [
                "Caíste de una altura muy alta, estás conmocionado y parece que estás herido internamente",
                "Recuerdas quién eres de golpe, Zhongli, exacto, eres el héroe legendario de la superficie",
                "Zhongli: claro, ahora lo recuerdo, estaba de expedición cuando una brecha de portal",
                "me absorbió al sub-suelo, es bastante diferente a las leyendas...",
                "Zhongli: Bueno, será mejor que comience a caminar por acá, hace frío a decir verdad...",
                "Opciones del destino", "1. Buscar una salida", "2. Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)"
            ],
            "buscar una salida": [
                "Te perdiste buscando la salida, sientes el frío comenzando a afectarte poco a poco...",
                "1. Rendirte ante el frío", "2. Seguir buscando una salida"
            ],
            "Explorar las catacumbas abandonadas del sub-suelo, (CAERLEON)": [
                "Ves una luz al final del túnel, deseas ir hacia ella?",
                "1. Ir hacia la luz", "2. Retroceder para buscar la salida"
            ],
            "Rendirte ante el frío": ["Moriste congelado"],
            "Seguir buscando una salida": [
                "A pesar de tu desespere de buscar la salida te perdiste en el vacio de la fronteras",
                "Sientes como la obscuridad te consume tu alma y finalmente te dejas consumir..."
            ],
            "Rechazar su oferta": [
                "Ah, es una lastima, total iba a consumir tu alma...",
                "El caballero te atraveso robandote el alma..."
            ],
            "Ir hacia la luz": [
                "Caes encima de la ciudad, es enorme y repleta de monstruos como personas, ves un puesto",
                "de comida a lo lejos y un castillo algo tétrico",
                "1. Ir a comer algo al puesto de comida", "2. Ir hacia el castillo a investigar sobre el pueblo"
            ],
            "Retroceder para buscar la salida": [
                "Caballero desconocido: hey, que haces aca pequeño humano?",
                "Zhongli: e-eh nada, justo me estaba por ir, adios",
                "Nah, tu no te vas... unete a mi chico, hazme caso...",
                "1. Aceptar su invitacion", "2. Rechazar su oferta"
            ],
            "Aceptar su invitacion": [
                "Sientes como se consume tu alma, el caballero se hace mas poderoso..."
            ],
            "Ir a comer algo al puesto de comida": [
                "Fuiste a comer al puesto de comida, eventualmente te sentiste mal y explotaste."
            ],
            "Ir hacia el castillo a investigar sobre el pueblo": [
                "Llegaste al castillo, es inmenso y repleto de estatuas en forma de monstruos",
                "Encuentras un monstruo de caballería",
                "1. Hablar con el monstruo", "2. Intentar pelear con el con tus habilidades mágicas"
            ],
            "Hablar con el monstruo": [
                "Te acercas para hablar con el monstruo, en tu plática te habla del reino Puertero: Este reino se formó hace ",
                "*ilegible* años, todo era pacífico hasta que el vacío se apoderó de las fronteras del reino",
                "Según la profecía un guerrero de aura carmesí nos librará de este fatídico final, y tal parece que ese eres tú.",
                "Zhongli: ¿YO!? ¿De qué hablas? soy un héroe de la superficie no de las catacumbas del sub-suelo",
                "1. Ayudar con la profesia", "2. Irse del lugar"
            ],
            "Intentar pelear con el con tus habilidades mágicas": [
                "El monstruo acabó contigo en tan solo un movimiento de brazo, patético"
            ],
            "Irse del lugar": [
                "Decides irte sin embargo el monstruo te ataca con su arma atravesándote"
            ],
            "Ayudar con la profesia": [
                "Perfecto, pasa adelante, mi rey te espera dentro, antes toma esto...",
                "Te entregó una espada legendaria...",
                "1. Ir hacia el rey"
            ],
            "Ir hacia el rey": [
                "Al llegar al salón real, el rey te observa atentamente.",
                "Zhongli: Rey, soy el héroe de la superficie y estoy aquí para ayudar con la profecía.",
                "Rey: Héroe de la superficie, nos has encontrado en tiempos oscuros. La corrupción se ha propagado por todo el reino.",
                "Zhongli: Dime, Rey, ¿qué debo hacer para liberar al reino de esta corrupción?",
                "Rey: Debes aventurarte a las fronteras y eliminar a los caballeros corruptos que las custodian.",
                "1. Continuar tu camino", "2. Esperar al rey"
            ],
            "Continuar tu camino": [
                "Sigues tu camino y te encuentras con un caballero monstruo corrupto.",
                "Zhongli: Debo enfrentarlo y limpiar esta tierra de corrupción.",
                "1. Atacar al caballero monstruo", "2. Esperar al rey"
            ],
            "Esperar al rey": [
                "Rey: Antes de enfrentarte a los caballeros corruptos, debes fortalecer tu espíritu.",
                "Zhongli: ¿Cómo puedo hacerlo, Rey?",
                "Rey: Ayudando a los aldeanos y eliminando pequeñas amenazas en el reino.",
                "1. Ayudar a eliminar la corrupción", "2. Negarse ya que no tienes nada que ver con ese reino"
            ],
            "Negarse ya que no tienes nada que ver con ese reino": [
                "Al escuchar esto el rey le ordena a tu guardia de tu ejecucion"
            ],
            "Ayudar a eliminar la corrupción": [
                "Luchas valientemente y eliminas a varios caballeros corruptos.",
                "Zhongli: He eliminado a varios caballeros corruptos. ¿Qué más debo hacer?",
                "Rey: Ahora debes enfrentarte a su líder, el caballero oscuro.",
                "1. Ir a cumplir tu mision..."
            ],
            "Ir a cumplir tu mision...": [
                "Te enfrentas al caballero oscuro en una batalla épica.",
                "Zhongli: ¡Esta es la batalla final!",
                "Con un golpe final, derrotas al caballero oscuro.",
                "1. Proclamarse victorioso..."
            ],
            "Proclamarse victorioso...": [
                "Legendary Ending. Victoria...",
                "Zhongli: ¡He salvado al reino y cumplido la profecía!"
            ]
        }

        for idx, text in enumerate(state_texts.get(self.state, [])):
            draw_text(text, 50, 30 + idx * 30)

game_state = GameState()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        game_state.handle_event(event)
    
    game_state.show()
    pygame.display.update()
