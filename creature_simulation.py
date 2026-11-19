class Creature:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp})"


class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power, depth=0):
        super().__init__(name, hp, attack_power)
        self.depth = depth

    def dive_to(self, new_depth):
        self.depth = new_depth
        print(f"{self.name} dives to depth {self.depth} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return
        print(f"{self.name} attacks {target.name} from underwater at depth {self.depth}m for {self.attack_power} damage!")
        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0


if __name__ == "__main__":
    shark = SwimmingCreature("Deep Shark", 60, 12)
    dummy = Creature("Practice Dummy", 40, 0)
    shark.dive_to(30)
    shark.attack(dummy)
    print(dummy)
