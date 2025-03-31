from Entity import Entity
from Shoot import shoot

class Character(Entity):
    def __init__(self, lives):
        super().__init__()
        self.lives = lives
        self.is_alive = lives > 0

    def move(self, direction):
        pass

    def shoot(self):
        shoot = shoot(self.x, self.y, direction="up")
        shoot.initialize()
        return shoot
    
    def collide(self, other_entity):
        if self.is_alive and other_entity.is_alive:
            if hasattr(other_entity, "is_enemy") and other_entity.is_enemy:
                self.lives -= 1
                if self.lives <= 0:
                    self.is_alive = False
                    print("Fin del juego, no quedan vidas.")
            if hasattr(other_entity, "is_boss") and other_entity.is_boss:
                self.lives = 0
                self.is_alive = False
                print("Fin del juego, el jefe derrotó al personaje.")

    def reset(self):

        self.lives = 3
        self.is_alive = True
        pass

    def __str__(self):
        return f"Character with {self.lives} lives, alive: {self.is_alive}, position: ({self.x}, {self.y}), image: {self.image}"