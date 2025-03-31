from Player import Player
from Opponent import Opponent
from Boss import Boss

class Game:
    def __init__(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False

    def start(self):
        self.is_running = True
        self.score = 0
        print("Juego iniciado")

    def update(self):
        if self.is_running:
            print("El juego se está actualizando")
        else:
            print("El juego no ha iniciado")

    def end_game(self):
        self.is_running = False
        print("Fin del juego")

    def reset(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False

    def spawn_player(self, player_name):
        if self.is_running:
            self.player = Player(name=player_name)
        else:
            print("El juego no se está ejecutando. No se puede crear el jugador.")
        self.player,lives = 3
        print(f"Jugador {self.player.name} inicializado con {self.player.lives}")
        self.player.score = 0
        self.player = Player(name=player_name)
        self.player.lives = 3
        print(f"Jugador {self.player.name} incializado con {self.player.lives}")

    def update_player(self):
        if self.is_running and self.player:
            print(f"Actualizando jugador {self.player.name}...")
            self.player.move()
            print(f"Jugador {self.player.name} se está moviendo.")
        else:
            print("El juego no se está ejecutando o no hay personaje para actualizar.")
        self.player = Player(name=player_name)
        self.player.lives = 3
        print(f"Jugador {self.player.name} initializado con {self.player.lives} vidas.")
        self.player.score = 0

    def spawn_opponent(self, opponent_type="regular", speed=1):
        if self.is_running:
            if opponent_type == "regular":
                self.opponent = Opponent(speed=speed)
                print(f"Oponente regular apareció con velocidad {speed}.")
            elif opponent_type == "boss":
                self.opponent = Boss(speed_multiplier=speed)
                print(f"Jefe apareció con multiplicador de velocidad {speed}.")
            else:
                print("Tipo de oponente no reconocido.")
        else:
            print("El juego no se está ejecutando. No se puede crear un oponente.")

    def __str__(self):
        return f"Estado de juego: puntuación = {self.score}, ejecución = {self.is_running}, jugador = {self.player}, oponente = {self.opponent}"
    
    def convert_enemy_to_star(self, enemy):
        if self.is_running and enemy:
            print(f"Enemigo {enemy} convertido en estrella!")
            self.score += 1
        else:
            print("El juego no se está ejecutando o el enemigo es inválido.")

    def initialize_lives(self, lives=3):
        self.lives = lives
        print(f"Jugador empieza con {self.lives} vidas.")

    def lose_life(self):
        if self.is_running and self.lives > 0:
            self.lives -= 1
            print(f"Jugador perdió una vida! Vidas restantes: {self.lives}")
            if self.lives == 0:
                print("No quedan vidas. Fin del juego!")
                self.end_game()
        else:
            print("El juego no se está ejecutando o no quedan vidas.")

    def spawn_boss(self):
        if self.is_running:
            self.opponent = Boss(speed_multiplier=2)
            print("Apareció un jefe! Se mueve el doble de rápido!")
        else:
            print("El juego no se está ejecutando. No se puede crear un jefe.")

    def display_score_and_lives(self):
        if self.is_running:
            print(f"Puntaje: {self.score}, Vidas: {self.lives}")
        else:
            print("El juego no se está ejecutando.")
    
    def remove_opponent(self):
        if self.is_running and self.opponent:
            print(f"Oponent {self.opponent} derrotado!")
            self.opponent = None
            self.spawn_boss()
        else:
            print("el juego no se está ejecutando o no quedan oponentes.")