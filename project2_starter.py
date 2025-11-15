"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [DeAundre Black]
Date: [11-14-2025]

AI Usage: ChatGPT helped me understand class structure and object-oriented concepts.
It also helped me organize and complete several TODO sections.
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple automated battle system used to test character functionality.
    Do NOT modify this class.
    """

    def __init__(self, character1, character2):
        """Stores references to the two characters that will battle."""
        self.char1 = character1
        self.char2 = character2

    def fight(self):
        """Runs a single round of attacks between the two characters."""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")

        # Display initial stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()

        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)

        # Only allow counterattack if opponent is alive
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)

        # Final stats
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()

        # Determine winner
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")


# ============================================================================
# YOUR CLASSES TO IMPLEMENT
# ============================================================================

import random  # Needed for Rogue's random crit chance


class Character:
    """
    Base class for all character types.
    Provides core stats and basic attack behavior.
    """

    def __init__(self, name, health, strength, magic):
        """Initialize the character's core attributes."""
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic

    def attack(self, target):
        """Performs a basic strength-based attack."""
        damage = self.strength
        target.take_damage(damage)

    def take_damage(self, damage):
        """Reduces health by the specified damage amount."""
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print("Character Defeated!")

    def display_stats(self):
        """Prints the character's stats in a clean format."""
        print(f"Character Name: {self.name}")
        print(f"Current Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")


class Player(Character):
    """
    Parent class for all player-controlled characters.
    Adds class type, level, and experience.
    """

    def __init__(self, name, character_class, health, strength, magic, current_level=1, exp=100):
        """
        Initialize a player character with class and progression data.
        Calls Character initializer for shared stats.
        """
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.current_level = current_level
        self.exp = exp
        self.level = current_level

    def display_stats(self):
        """Displays both standard character stats and player-specific attributes."""
        super().display_stats()
        print(f"Class: {self.character_class}")
        print(f"Level: {self.current_level}")
        print(f"Experience: {self.exp}")


class Warrior(Player):
    """
    Warrior class - specializes in strong physical attacks.
    """

    def __init__(self, name):
        """Creates a Warrior with high health and strength."""
        super().__init__(name=name, character_class="Warrior", health=120, strength=20, magic=5)

    def attack(self, target):
        """Warrior basic attack that consumes strength and deals scaled damage."""
        if self.strength >= 4:
            self.strength -= 4
            damage = self.strength * 0.7
            target.health -= damage
        else:
            print("Low strength, not enough to attack")

    def power_strike(self, target):
        """Powerful Warrior attack that uses more strength and deals heavy damage."""
        if self.strength >= 7:
            self.strength -= 7
            damage = self.strength * 1.75
            target.health -= damage
        else:
            print("Not enough strength to use Power Strike")


class Mage(Player):
    """
    Mage class - specializes in magic attacks and spells.
    """

    def __init__(self, name):
        """Creates a Mage with high magic but lower physical strength."""
        super().__init__(name, character_class="Mage", health=85, strength=10, magic=25)

    def attack(self, target):
        """Basic magic attack that uses a small amount of magic."""
        if self.magic >= 3:
            self.magic -= 3
            damage = self.magic * 0.4
            target.health -= damage
        else:
            print("Not enough magic left to attack")

    def fireball(self, target):
        """Mage's powerful fireball spell using a larger magic cost."""
        if self.magic >= 6:
            self.magic -= 6
            damage = self.magic * 1.2
            target.health -= damage
        else:
            print("Not enough magic to cast Fireball")


class Rogue(Player):
    """
    Rogue class - agile attacker with critical strike abilities.
    """

    def __init__(self, name):
        """Creates a Rogue with balanced stats and crit-focused skills."""
        super().__init__(name=name, character_class="Rogue", health=90, strength=15, magic=15)

    def attack(self, target):
        """Rogue attack with a 30% chance to deal double damage."""
        base_damage = self.strength * 0.75
        crit_roll = random.randint(1, 10)

        if crit_roll <= 3:
            damage = base_damage * 2
            print("Critical Hit!")
        else:
            damage = base_damage

        target.health -= damage

    def sneak_attack(self, target):
        """Guaranteed critical hit — Rogue special move."""
        base_damage = self.strength * 0.7
        damage = base_damage * 2
        print("Sneak attack hit!")
        target.health -= damage


class Weapon:
    """
    Weapon class used for composition (characters can carry a weapon).
    Each weapon provides a damage bonus.
    """

    def __init__(self, name, damage_bonus):
        """Store the weapon's name and its bonus damage."""
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        """Prints weapon information."""
        print(f"Weapon Name: {self.name}")
        print(f"Damage Bonus: {self.damage_bonus}")


# ============================================================================
# MAIN PROGRAM FOR TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)

    # Create sample characters
    warrior = Warrior("Sir Galahad")
    mage = Mage("T DA WIZARD")
    rogue = Rogue("Robin Hood")

    # Show their stats
    print("\nCharacter Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    # Polymorphism test: each class has its own attack behavior
    print("\nTesting Polymorphism (same attack method, different results):")
    dummy_target = Character("Target Dummy", 100, 0, 0)

    for character in [warrior, mage, rogue]:
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset for next test

    # Test unique abilities
    print("\nTesting Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)

    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)

    # Weapon tests
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)

    sword.display_info()
    staff.display_info()
    dagger.display_info()

    # Battle system test
    print("\nTesting Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()

    print("\n✅ Testing complete!")
