from Entity import Entity

class shoot(Entity):

    def __init__(self, x, y, image, speed):

        super().__init__(x, y, image)
        self.speed = speed
        self.is_alive = True
        self.is_star = False
        self.is_bomb = False
        self.is_bomb_exploded = False

    def __str__(self):

        return f"shoot at ({self.x}, {self.y}) with speed {self.speed}, alive: {self.is_alive}, star: {self.is_star}, bomb: {self.is_bomb}"
            
    def move(self):
        pass

    def hit_target(self):
        pass

    def explode(self):
        pass

    def reset(self):

        self.is_alive = True
        self.is_star = False
        self.is_bomb = False
        self.is_bomb_exploded = False
        self.x = 0
        self.y = 0
        self.speed = 0

    def serialize(self):
        
        data = super().serialize()
        data.update({
            "speed": self.speed,
            "is_alive": self.is_alive,
            "is_star": self.is_star,
            "is_bomb": self.is_bomb,
            "is_bomb_exploded": self.is_bomb_exploded
        })
        return data
    def deserialize(self, data):
        
        super().deserialize(data)
        self.speed = data["speed"]
        self.is_alive = data["is_alive"]
        self.is_star = data["is_star"]
        self.is_bomb = data["is_bomb"]
        self.is_bomb_exploded = data["is_bomb_exploded"]