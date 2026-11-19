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


class FireCreature(Creature):
    def __init__(self, name, hp, attack_power, fire_level=50):
        super().__init__(name, hp, attack_power)
        self.fire_level = max(0, min(100, fire_level))

    def emit_fire(self, new_fire_level):
        self.fire_level = max(0, min(100, new_fire_level))
        print(f"{self.name} sets fire level to {self.fire_level}!")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return
        total_damage = self.attack_power + (self.fire_level // 10)
        print(f"{self.name} breathes fire (level {self.fire_level}) at {target.name} for {total_damage} damage!")
        target.hp -= total_damage
        if target.hp < 0:
            target.hp = 0


if __name__ == "__main__":
    hawk = FlyingCreature("Sky Hawk", 50, 8)
    shark = SwimmingCreature("Deep Shark", 60, 12)
    drake = FireCreature("Flame Drake", 70, 10, fire_level=40)
    dummy = Creature("Practice Dummy", 100, 0)

    hawk.fly_to(120)
    hawk.attack(dummy)

    shark.dive_to(30)
    shark.attack(dummy)

    drake.emit_fire(80)
    drake.attack(dummy)

    print(dummy)
