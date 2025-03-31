from Character import Character

class Opponent(Character):
    def __init__(self, is_star = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_star = is_star

    def move(self):
        pass

    def shoot(self):
        pass

    def collide(self, other_entity):
        if other_entity.type == "player_bullet":
            self.is_alive = False
            other_entity.owner.score += 1  # Increment the player's score
        pass

    def reset(self):
        self.lives = 3
        self.is_alive = True
        pass
 
    def serialise(self):
        data = super().serialise()
        data.update({
            "is_star": self.is_star
        })
        return data
  
    def deserialise(self, data):
        super().deserialise(data)
        self.is_star = data["is_star"]
 
    def __str__(self):
        return f"Oponente con {self.lives} vidas y is_star={self.is_star}"
    