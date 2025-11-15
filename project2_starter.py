"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Your Name Here]
Date: [Date]

AI Usage: [CHATGPT help me with understanding classes while also helping me with structure in the todo sections]
"""


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
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")


# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

# AI USAGE (1): Used AI throughout program to check for correct syntax/any errors I had in my code.
# AI USAGE (2): Used AI to explain any tasks that I was confused about to make sure I knew what I was doing.
# AI USAGE (3): Used AI to help me apply certain calculations that I couldn't figure out how to type out.
# AI USAGE: AI platform used: ChatGPT

import random


# Asked ChatGPT to explain this part: Line 275 uses random, needed to import the random module for it to run.

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """

    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        """Initialize basic character attributes"""
        # TODO: Set the character's name, health, strength, and magic
        # These should be stored as instance variables

    def attack(self, target):
        damage = self.strength  # damage based on self.strength
        target.take_damage(damage)  # used to apply damage

        """
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """
        # TODO: Implement basic attack
        # Damage should be based on self.strength
        # Use target.take_damage(damage) to apply damage

    def take_damage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:  # makes sure health doesn't pass below zero
            self.health = 0

        if self.health == 0:
            print("Character Defeated!")
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        # TODO: Implement taking damage
        # Reduce self.health by damage amount
        # Make sure health doesn't go below 0

    def display_stats(self):
        print(f"Character Name: {self.name}")
        print(f"Current Health {self.health}")
        print(f"Current Strength: {self.strength}")
        print(f"Current Magic: {self.magic}")
        """
        Prints the character's current stats in a nice format.
        """
        # TODO: Print character's name, health, strength, and magic
        # Make it look nice with formatting


class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """

    def __init__(self, name, character_class, health, strength, magic, current_level=1, exp=100):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.current_level = current_level
        self.exp = exp
        self.level = current_level
        """
        Initialize a player character.
        Should call the parent constructor and add player-specific attributes.
        """
        # TODO: Call super().__init__() with the basic character info
        # TODO: Store the character_class (like "Warrior", "Mage", etc.)
        # TODO: Add any other player-specific attributes (level, experience, etc.)

    def display_stats(self):
        super().display_stats()

        print(f"Character Class: {self.character_class}")
        print(f"Character's Current Level: {self.current_level}")
        print(f"Character's Experience Level: {self.exp}")

        """
        Override the parent's display_stats to show additional player info.
        Should show everything the parent shows PLUS player-specific info.
        """
        # TODO: Call the parent's display_stats method using super()
        # TODO: Then print additional player info like class and level


class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """

    # Used certain suggested stats for characters
    def __init__(self, name):
        super().__init__(name=name, character_class="Warrior", health=120, strength=20, magic=5)

    """
    Create a warrior with appropriate stats.
    Warriors should have: high health, high strength, low magic
    """

    # TODO: Call super().__init__() with warrior-appropriate stats
    # Suggested stats: health=120, strength=15, magic=5

    def attack(self, target):
        if self.strength >= 4:  # Makes sure they have enough strength to use attacks
            self.strength -= 4
            damage = self.strength * 0.7  # damage multiplier for warrior class base attacks is 0.7
            target.health -= damage
        else:
            print("Low strength, not enough to attack")

        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        # TODO: Implement warrior attack
        # Should do more damage than basic attack
        # Maybe strength + 5 bonus damage?

    def power_strike(self, target):
        if self.strength >= 7:  # Makes sure they have enough magic
            self.strength -= 7
            damage = self.strength * 1.75  # damage multiplier for base attacks is 0.4
            target.health -= damage
        else:
            print("Too much strength used! Not enough left to use power strike")

        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        # TODO: Implement power strike
        # Should do significantly more damage than regular attack


class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """

    def __init__(self, name):
        super().__init__(name, character_class="Mage", health=85, strength=10, magic=25)  # base stats
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """
        # TODO: Call super().__init__() with mage-appropriate stats
        # Suggested stats: health=80, strength=8, magic=20

    def attack(self, target):
        if self.magic >= 3:  # Makes sure they have enough magic
            self.magic -= 3
            damage = self.magic * 0.4  # damage multiplier for base attacks is 0.4
            target.health -= damage
        else:
            print("Not enough magic left to attack")
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        # TODO: Implement mage attack
        # Should use self.magic for damage calculation instead of strength

    def fireball(self, target):
        if self.magic >= 6:  # Stronger attack = higher magic consumption
            self.magic -= 6
            damage = self.magic * 1.2  # Stronger attack also = higher damage multiplier
            target.health -= damage
        else:
            print("Not enough magic to use fireball")
        """
        Special mage ability - a powerful magical attack.
        """
        # TODO: Implement fireball spell
        # Should do magic-based damage with bonus


class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """

    def __init__(self, name):
        super().__init__(name=name, character_class="Rogue", health=90, strength=15, magic=15)

        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """
        # TODO: Call super().__init__() with rogue-appropriate stats
        # Suggested stats: health=90, strength=12, magic=10

    def attack(self, target):
        basic_attack = self.strength * 0.75
        critical_chance = random.randint(1, 10)

        if critical_chance <= 3:
            damage = basic_attack * 2
            print("Critical Hit!")
        else:
            damage = basic_attack

        target.health -= damage

        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        # TODO: Implement rogue attack
        # Could add a chance for critical hit (double damage)
        # Hint: use random.randint(1, 10) and if result <= 3, it's a crit

    def sneak_attack(self, target):
        base_attack = self.strength * 0.7
        sneak_damage = base_attack * 2
        print("Sneak attack hit!")

        target.health -= sneak_damage

        """
        Special rogue ability - guaranteed critical hit.
        """
        # TODO: Implement sneak attack
        # Should always do critical damage


class Weapon:

    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus

    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """

    """
    Create a weapon with a name and damage bonus.
    """

    # TODO: Store weapon name and damage bonus

    def display_info(self):
        print(f"Weapon Name: {self.name}")
        print(f"Damage Bonus: {self.damage_bonus}")
        """
        Display information about this weapon.
        """
        # TODO: Print weapon name and damage bonus


# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)

    # TODO: Create one of each character type
    # warrior = Warrior("Sir Galahad")
    # mage = Mage("Merlin")
    # rogue = Rogue("Robin Hood")
    warrior = Warrior("Sir Galahad")
    mage = Mage("T DA WIZARD")
    rogue = Rogue("Robin Hood")

    # TODO: Display their stats
    # print("\n📊 Character Stats:")
    # warrior.display_stats()
    # mage.display_stats()
    # rogue.display_stats()

    print("\n Character Stats:")
    warrior.display_stats()

    mage.display_stats()

    rogue.display_stats()

    # TODO: Test polymorphism - same method call, different behavior
    # print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    # dummy_target = Character("Target Dummy", 100, 0, 0)
    print("\n Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)

    # for character in [warrior, mage, rogue]:
    #     print(f"\n{character.name} attacks the dummy:")
    #     character.attack(dummy_target)
    #     dummy_target.health = 100  # Reset dummy health

    for character in [warrior, mage, rogue]:
        character.attack(dummy_target)
        dummy_target.health = 100
    #
    # TODO: Test special abilities
    # print("\n✨ Testing Special Abilities:")
    # target1 = Character("Enemy1", 50, 0, 0)
    # target2 = Character("Enemy2", 50, 0, 0)
    # target3 = Character("Enemy3", 50, 0, 0)
    print("\n Testing Special Abilities")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)

    # warrior.power_strike(target1)
    # mage.fireball(target2)
    # rogue.sneak_attack(target3)
    warrior.power_strike(target1)

    mage.fireball(target2)

    rogue.sneak_attack(target3)

    # TODO: Test composition with weapons
    # print("\n🗡️ Testing Weapon Composition:")
    # sword = Weapon("Iron Sword", 10)
    # staff = Weapon("Magic Staff", 15)
    # dagger = Weapon("Steel Dagger", 8)

    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    #
    # sword.display_info()
    # staff.display_info()
    # dagger.display_info()

    sword.display_info()

    staff.display_info()

    dagger.display_info()
    # TODO: Test the battle system
    # print("\n⚔️ Testing Battle System:")
    # battle = SimpleBattle(warrior, mage)
    # battle.fight()

    print("\n Testing Battle System:")

    battle = SimpleBattle(warrior, mage)

    battle.fight()


    print("\n✅ Testing complete!")