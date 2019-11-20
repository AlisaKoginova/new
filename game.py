from random import randint

class Unit:
    def __init__(self, name, hp, armor, dmg, delta_dmg):
        self.name = name
        print(f'Unit {self.name} is created.')
        self.hp = hp
        self.armor = armor
        self.dmg = dmg
        self.delta_dmg = delta_dmg

    def name_getter(self):
        return self._name

    def name_setter(self, name):
        self._name = name if isinstance(name, str) else 'Nameless'

    name = property(name_getter, name_setter)

    def hp_getter(self):
        return self._hp

    def hp_setter(self, hp):
        self._hp = hp if hp > 0 else 0
        print(f'{self.name} hp = {self.hp}.')

    hp = property(hp_getter, hp_setter)

    def armor_getter(self):
        return self._armor

    def armor_setter(self, armor):
        self._armor = armor if armor > 0 else 0
        print(f'{self.name} armor = {self.armor}.')

    armor = property(armor_getter, armor_setter)

    def dmg_getter(self):
        return self._dmg

    def dmg_setter(self, dmg):
        self._dmg = dmg if dmg > 0 else 0
        print(f'{self.name} dmg = {self.dmg}.')

    dmg = property(dmg_getter, dmg_setter)

    def delta_dmg_getter(self):
        return self._delta_dmg

    def delta_dmg_setter(self, delta_dmg):
        self._delta_dmg = delta_dmg if delta_dmg > 0 else 0

    delta_dmg = property(delta_dmg_getter, delta_dmg_setter)

    def attack(self, enemy):
        if isinstance(enemy, Unit):
            attack_dmg = randint(self.dmg-self.delta_dmg, self.dmg + self.delta_dmg)
            print(f'{self.name} attacked. Dmg = {attack_dmg}')
            enemy.defence(attack_dmg)
        else:
            print('Enemy must be Unit type.')

    def defence(self, dmg):
        if self.armor < dmg:
            self.hp = self.hp + self.armor - dmg
            if not self.is_alive():
                print(f'{self.name} is dead.')
        else:
            print(f'Armor fully saves {self.name}. Hp still = {self.hp}')

    def is_alive(self):
        if self.hp:
            return True
        else:
            return False

    def wear_item(self, item):
        if isinstance(item, Item):
            print(f'-----------{self.name} wears {item.item_name}-----------')
            if item.dmg_boost:
                print(f'Now {self.name} dmg is increased by {item.dmg_boost}')
                self.dmg += item.dmg_boost
                return
            if item.armor_boost:
                print(f'Now {self.name} armor is increased by {item.armor_boost}.')
                self.armor += item.armor_boost
                return
        else:
            print('Item must be Item type.')

class Battle:
    @classmethod
    def start_battle(self, unit1, unit2, rand_boost):
        if isinstance(unit1, Unit) and isinstance(unit2, Unit):
            print('------------------Battle begins------------------')
            # добавление случаного коэффициента
            # добавление случаного коэффициента
            # добавление случаного коэффициента
            unit1.dmg += randint(0, rand_boost)
            unit1.armor += randint(0, rand_boost)
            unit2.dmg += randint(0, rand_boost)
            unit2.armor += randint(0, rand_boost)
            while True:
                if unit1.is_alive():
                    unit1.attack(unit2)
                else:
                    print(f'{unit2.name} wins!')
                    break
                if unit2.is_alive():
                    unit2.attack(unit1)
                else:
                    print(f'{unit1.name} wins!')
                    break
        else:
            print('Battle should be between 2 Units.')

class Item:
    def __init__(self, item_name, dmg_boost, armor_boost):
        self.item_name = item_name
        self.dmg_boost = dmg_boost
        self.armor_boost = armor_boost

    def dmg_boost_getter(self):
        return self._dmg_boost

    def dmg_boost_setter(self, dmg_boost):
        self._dmg_boost = dmg_boost if dmg_boost > 0 else 0

    dmg_boost = property(dmg_boost_getter, dmg_boost_setter)

    def armor_boost_getter(self):
        return self._armor_boost

    def armor_boost_setter(self, armor_boost):
        self._armor_boost = armor_boost if armor_boost > 0 else 0

    armor_boost = property(armor_boost_getter, armor_boost_setter)

ogre = Unit('Ogre', 25, 10, 15, 3)
elf = Unit('Elf', 15, 5, 7, 5)
sword = Item('Silver sword', 10, 0)
helmet = Item('Magic helmet', 0, 12)
elf.wear_item(helmet)
ogre.wear_item(sword)
Battle.start_battle(ogre, elf, 10)



