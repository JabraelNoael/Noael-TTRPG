class Player:
    def __init__(self, name: str, age: int) -> None:
        pass
        self.name: str = name
        self.age: int = age


Michael: Player = Player(age=18,name="Michael")


print(Michael.name)