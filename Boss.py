from Opponent import Opponent

class Boss(Opponent):
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed * 2) 

    def special_attack(self):
        print("El jefe final realiza un ataque especial devastador.")

    def reset(self):
        super().reset()
        print("El jefe final ha sido reseteado.")
   
    def serialise(self):

        data = super().serialise()
        data.update({
            "special_attack": self.special_attack
        })
        return data
    
    def deserialise(self, data):

        super().deserialise(data)
        self.special_attack = data["special_attack"]

    def __str__(self):

        return f"Jefe Final en ({self.x}, {self.y}) con velocidad {self.speed}"
    
    def move(self):
        print(f"El jefe final se mueve a ({self.x}, {self.y})")
    
    def hit_target(self):
        print("El jefe final ha golpeado un objetivo.")

    def take_damage(self, damage):
        self.health -= damage
        print(f"El jefe final recibe {damage} de daño. Salud restante: {self.health}")
        if self.health <= 0:
            self.defeated()

    def defeated(self):
        print("Jefe final derrotado")