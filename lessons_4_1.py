from enum import Enum
from random import randint, choice
import random


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    SAVE_DAMAGE_AND_REVERT = 4
    STUN = 5
    RESURRECTION = 6
    ACCEPT_DAMAGE = 7


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super(Boss, self).__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        chosen_hero = choice(heroes)
        self.__defence = chosen_hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super(Boss, self).__str__() + f' defence: {self.defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super(Hero, self).__init__(name, health, damage)
        if not isinstance(ability, SuperAbility):
            raise ValueError('Value for attribute ability must be of type SuperAbility')
        else:
            self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super(Warrior, self).__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        corfficient = randint(2, 5)
        boss.health -= self.damage * corfficient
        print(f'Warrior hits critically: {self.damage * corfficient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super(Magic, self).__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        pass


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super(Medic, self).__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super(Berserk, self).__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__saved_damage = 0

    def apply_super_power(self, boss, heroes):
        self.damage += boss.damage // 5
        print(f"Berserk revert damage  {self.damage}")

class Thor(Hero):
    def __init__(self, name, health, damage):
        super(Thor, self).__init__(name, health, damage, SuperAbility.STUN)

    def apply_super_power(self, boss, heroes):
        stun = [1, 2, 3]
        b = random.choice(stun)
        if b == 1:
            boss.damage = 0
            print("STUN BOSS")
        else:
            boss.damage = 50 - 1


class Witcher(Hero):
    def __init__(self, name, health, damage=0):
        super(Witcher, self).__init__(name, health, damage, SuperAbility.RESURRECTION)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health <= 0 < boss.health:
                hero.health += self.health
                self.health = 0
                print(f'The witcher sacrificed his life')



class Golem(Hero):
    def __init__(self, name, health, damage, protection=0):
        super(Golem, self).__init__(name, health, damage, SuperAbility.ACCEPT_DAMAGE)
        self.protection = protection

    def apply_super_power(self, boss, heroes):
        print(f"protection: {self.protection}")
        for hero in heroes:
            if hero.health > 0:
                self.protection = boss.damage // 5
                hero.apply_super_power(boss, heroes)
                if boss.damage >= 1:
                    hero.health += self.protection
                else:
                    hero.health -= boss.damage
round_number = 0


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def print_statistics(boss, heroes):
    print(f'-----------ROUND {round_number} -----------')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if boss.defence != hero.ability and hero.health > 0:
            hero.attack(boss)

    print_statistics(boss, heroes)


def start_game():
    boss = Boss("Surtur", 3000, 50)
    warrior = Warrior("Spartak", 270, 20)
    doc = Medic("Merlin", 250, 5, 15)
    magic = Magic("Harry Potter", 260, 20)
    berserk = Berserk("Kilua", 280, 25)
    assistant = Medic("Stajer", 290, 10, 5)
    thor = Thor("Odin", 300, 20)
    witcher = Witcher("Nanako", 300)
    golem = Golem("Grud", 300, 15)

    heroes_list = [warrior, doc, magic, berserk, assistant, thor, witcher, golem]

    print_statistics(boss, heroes_list)
    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
