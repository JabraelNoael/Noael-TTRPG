class Item:
    def __init__(self, name: str, description: str) -> None:
        self.name: str = name
        self.description: str = description

class Ability:
    def __init__(self, name: str, description: str, passive: bool) -> None:
        self.passive = passive
        self.name: str = name
        self.description: str = description

class Attributes:
    def __init__(self) -> None:
        # Health & Mana
        self.health: float = 100
        self.healthMax: float = 100
        self.healthRegen: float = self.healthMax/16 #per turn
        self.vitality: float = 5
        self.mana: float = 100
        self.manaMax: float = 100
        self.manaRegen: float = self.healthMax/9 #per turn
        # Character
        self.level: int = 1
        self.experience: float = 0
        # Crowd Control
        self.willpower: float = 5
        self.tenacity: float = 5
        # Combat
        self.initiative: float = 5
        self.speed: float = 5
        self.reach: float = 1
        # Attack
        ## Physical
        self.attack: float = 10
        self.criticalScale: float = 1.5
        self.bludgeon: float = 5
        self.pierce: float = 5
        self.slash: float = 5
        ### Pen
        self.physicalPenetration: float = 0
        self.bludgeonPenetration: float = 0
        self.piercePenetration: float = 0
        self.slashPenetration: float = 0
        self.physicalPenCap: float = 0.75
        self.bludgeonPenCap: float = 0.75
        self.piercePenCap: float = 0.75
        self.slashPenCap: float = 0.75
        ## Magical
        self.magic: float = 10
        self.arcana: float = 5
        self.aether: float = 5
        self.ethereal: float = 5
        self.ichor: float = 5
        self.magiaPool: float = 5
        # Defense
        ## Physical
        self.armorClass: float = 10
        self.defense: float = 5
        self.physicalResistance: float = 0
        self.bludgeonResist: float = 0
        self.pierceResist: float = 0
        self.slashResist: float = 0
        self.physicalResistCap: float = 0.75
        self.bludgeonResistCap: float = 0.75
        self.pierceResistCap: float = 0.75
        self.slashResistCap: float = 0.75
        ## Magical
        self.ward: float = 0
        self.arcanaWard: float = 0
        self.aetherWard: float = 0
        self.etherealWard: float = 0
        self.ichorWard: float = 0
        # Other
        self.luck: float = 5
        self.partySize: int = 1

class Inventory:
    def __init__(self) -> None:
        self.items: list[str] = []

    def addItem(self, item: Item) -> None:
        self.items.append(item.name)

class Player:
    def __init__(self, name: str, age: int) -> None:
        pass
        self.name: str = name
        self.age: int = age
        self.attributes: Attributes = Attributes()
        self.inventory: Inventory = Inventory()