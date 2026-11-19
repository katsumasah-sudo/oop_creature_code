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


class FlyingCreature(Creature):
    def __init__(self, name, hp, attack_power, altitude=0):
        super().__init__(name, hp, attack_power)
        self.altitude = altitude

    def fly_to(self, new_altitude):
        self.altitude = new_altitude
        print(f"{self.name} flies to altitude {self.altitude} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return
        print(f"{self.name} swoops down from altitude {self.altitude}m to attack {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0


if __name__ == "__main__":
    hawk = FlyingCreature("Sky Hawk", 50, 8)
    dummy = Creature("Practice Dummy", 40, 0)
    hawk.fly_to(120)
    hawk.attack(dummy)
    print(dummy)
