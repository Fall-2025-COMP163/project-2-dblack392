"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [DeAundre Black]
Date: [11-14-2025]

AI Usage: ChatGPT helped me implement the class hierarchy (Character, Player, Warrior, Mage, Rogue, Weapon),
basic attacks, special abilities, and the testing code in main. They also helped me with a little bit of structure and comments I missed. I reviewed and edited the code myself.
"""

import random  # Used for Rogue critical hit chance


# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """

    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2

    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")

        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()

        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)

        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)

        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()

        if self.char1.health > self.char2.health:
            print(f" {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f" {self.char2.name} wins!")
        else:
            print("It's a tie!")


# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """

    def __init__(self, name, health, strength, magic):
        #Initialize basic character attributes
        # Store basic stats as instance variables
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic

    def attack(self, target):

        # Base damage comes from strength
        damage = self.strength

        # If this character has a weapon with a damage bonus, add it (composition)
        if hasattr(self, "weapon") and self.weapon is not None:
            damage += self.weapon.damage_bonus

        print(f"{self.name} attacks with a basic strike for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        # Subtract damage from health
        self.health -= damage

        # Make sure health doesn't go below 0
        if self.health < 0:
            self.health = 0

        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        print(f"\n--- {self.name} ---")
        print(f"Health  : {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic   : {self.magic}")


class Player(Character):
    #Base class for player characters.
    Inherits from Character and adds player-specific features.


    def __init__(self, name, character_class, health, strength, magic):

        #Initialize a player character.
        #Calls the parent constructor and adds player-specific attributes.

        # Call the parent constructor to set name, health, strength, magic
        super().__init__(name, health, strength, magic)

        # Store the player's class (e.g., "Warrior", "Mage", "Rogue")
        self.character_class = character_class

        # Add player-specific attributes
        self.level = 1
        self.experience = 0

        # Composition: players can HAVE a weapon
        self.weapon = None

    def equip_weapon(self, weapon):
        #Assign a weapon to this player
        self.weapon = weapon
        print(f"{self.name} equipped {weapon.name} (+{weapon.damage_bonus} damage).")

    def display_stats(self):

        #Override the parent's display_stats to show additional player info.
       #Shows everything the parent shows PLUS player-specific info.
        # Call the parent version first
        super().display_stats()

        # Then add player-specific information
        print(f"Class   : {self.character_class}")
        print(f"Level   : {self.level}")
        print(f"XP      : {self.experience}")


class Warrior(Player):

    #Warrior class - strong physical fighter.
    Inherits from Player.


    def __init__(self, name):
        #Create a warrior with appropriate stats.
        #Warriors: high health, high strength, low magic
        #Suggested stats: health=120, strength=15, magic=5

        super().__init__(name, "Warrior", health=120, strength=15, magic=5)

    def attack(self, target):
        #Override the basic attack to make it warrior-specific.
        #Warriors do extra physical damage.

        base_damage = self.strength + 5  # flat bonus for warriors

        # Include weapon bonus if equipped
        if self.weapon is not None:
            base_damage += self.weapon.damage_bonus

        print(f"{self.name} performs a heavy warrior attack for {base_damage} damage!")
        target.take_damage(base_damage)

    def power_strike(self, target):
        #Special warrior ability - a powerful attack that does extra damage.
        damage = self.strength * 2  # significantly more damage

        if self.weapon is not None:
            damage += self.weapon.damage_bonus

        print(f" {self.name} uses POWER STRIKE for {damage} damage!")
        target.take_damage(damage)


class Mage(Player):
    #Mage class - magical spellcaster.
    #Inherits from Player.

    def __init__(self, name):
        #Create a mage with appropriate stats.
        #Mages: low health, low strength, high magic
        #Suggested stats: health=80, strength=8, magic=20
        super().__init__(name, "Mage", health=80, strength=8, magic=20)

    def attack(self, target):
        #Override the basic attack to make it magic-based.
       #Mages use magic for damage instead of strength.

        damage = self.magic  # magic-based attack

        if self.weapon is not None:
            damage += self.weapon.damage_bonus

        print(f"{self.name} casts a magic bolt for {damage} damage!")
        target.take_damage(damage)

    def fireball(self, target):
        #Special mage ability - a powerful magical attack.
        damage = self.magic + 10  # stronger than normal attack

        if self.weapon is not None:
            damage += self.weapon.damage_bonus

        print(f" {self.name} casts FIREBALL for {damage} damage!")
        target.take_damage(damage)


class Rogue(Player):
    #Rogue class - quick and sneaky fighter.

    def __init__(self, name):
        """
        Create a rogue with appropriate stats.
        Rogues: medium health, medium strength, medium magic
        Suggested stats: health=90, strength=12, magic=10
        """
        super().__init__(name, "Rogue", health=90, strength=12, magic=10)

    def attack(self, target):
        #Override the basic attack to make it rogue-specific.
        #Rogues have a chance for a critical hit (double damage).
        #Hint: use random.randint(1, 10) and if result <= 3, it's a crit
        # Roll a random number to see if we crit (30% chance)
        roll = random.randint(1, 10)
        damage = self.strength

        if self.weapon is not None:
            damage += self.weapon.damage_bonus

        if roll <= 3:
            # Critical hit
            damage *= 2
            print(f" {self.name} lands a CRITICAL hit for {damage} damage!")
        else:
            print(f"{self.name} strikes swiftly for {damage} damage.")

        target.take_damage(damage)

    def sneak_attack(self, target):
        #Special rogue ability - guaranteed critical hit.
        damage = self.strength * 2

        if self.weapon is not None:
            damage += self.weapon.damage_bonus

        print(f"️ {self.name} uses SNEAK ATTACK for {damage} damage (guaranteed crit)!")
        target.take_damage(damage)


class Weapon:
    #Weapon class to demonstrate composition.
    #Characters can HAVE weapons (composition, not inheritance).

    def __init__(self, name, damage_bonus):
        #Create a weapon with a name and damage bonus.
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        #Display information about this weapon.
        print(f"Weapon: {self.name} (Damage Bonus: +{self.damage_bonus})")


# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)

    # Create one of each character type
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")

    # Display their stats
    print("\n Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    # Test polymorphism - same method call, different behavior
    print("\n Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)

    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset dummy health

    # Test special abilities
    print("\n Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)

    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)

    # Test composition with weapons
    print("\n Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)

    sword.display_info()
    staff.display_info()
    dagger.display_info()

    # Equip weapons and attack again
    print("\n️ Equipping Weapons and Attacking:")
    warrior.equip_weapon(sword)
    mage.equip_weapon(staff)
    rogue.equip_weapon(dagger)

    dummy_target.health = 100
    print(f"\n{warrior.name} attacks the dummy with a weapon:")
    warrior.attack(dummy_target)

    dummy_target.health = 100
    print(f"\n{mage.name} attacks the dummy with a weapon:")
    mage.attack(dummy_target)

    dummy_target.health = 100
    print(f"\n{rogue.name} attacks the dummy with a weapon:")
    rogue.attack(dummy_target)

    # Test the battle system
    print("\n Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()

    print("\n Testing complete!")
