from Character import Character

class Player(Character):
    def __init__(self, name, score = 0, lives = 3):
        super().__init__(name)
        self.score = score
        self.lives = lives

    def move(self, direction):
        print(f"{self.name} se mueve a {direction}")

    def shoot(self):
        print(f"{self.name} dispara!")