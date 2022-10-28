from enum import Enum
from random import randint, choice


class SuperAbility(Enum):
    STUN = 5
    KEEL_THEFT = 6


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



class Hacker(Hero):
    def __int__(self, name, health, damage):
        super(Hacker, self).__int__(name, health, damage, SuperAbility.KEEL_THEFT)

    def apply_super_power(self, boss, heroes):
        pass



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


class Thor(Hero):
    def __int__(self, name, health, damage):
        super(Thor, self).__int__(name, health, damage, SuperAbility.STUN)

    def apply_super_power(self, boss, heroes):
        pass


class Hacker(Hero):
    def __int__(self, name, health, damage):
        super(Hacker, self).__int__(name, health, damage, SuperAbility.KEEL_THEFT)

    def apply_super_power(self, boss, heroes):
        pass



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
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)
