import time
from enum import Enum
import random

class OmeletStyle(Enum):
    FRENCH = "French"
    SPANISH = "Spanish"
    JAPANESE = "Japanese"
    ITALIAN = "Italian"
    AMERICAN = "American"

class OmeletCooker:
    def __init__(self):
        self.ingredients = {
            OmeletStyle.FRENCH: ["eggs", "butter", "salt", "pepper", "chives"],
            OmeletStyle.SPANISH: ["eggs", "olive oil", "potatoes", "onions", "bell peppers"],
            OmeletStyle.JAPANESE: ["eggs", "soy sauce", "mirin", "dashi", "green onions"],
            OmeletStyle.ITALIAN: ["eggs", "olive oil", "tomatoes", "basil", "mozzarella"],
            OmeletStyle.AMERICAN: ["eggs", "butter", "cheese", "bacon", "mushrooms"]
        }
        
        self.cooking_styles = {
            OmeletStyle.FRENCH: "folded and fluffy",
            OmeletStyle.SPANISH: "thick with potatoes",
            OmeletStyle.JAPANESE: "rolled and sweet",
            OmeletStyle.ITALIAN: "open-faced with fresh ingredients",
            OmeletStyle.AMERICAN: "loaded with fillings"
        }

    def prepare_ingredients(self, style):
        print(f"\nPreparing ingredients for {style.value} omelet:")
        for ingredient in self.ingredients[style]:
            print(f"- Adding {ingredient}")
            time.sleep(0.5)

    def cook_omelet(self, style):
        print(f"\nCooking {style.value} style omelet:")
        steps = [
            "Heating the pan",
            "Adding the base ingredients",
            "Cooking the eggs",
            f"Preparing in {self.cooking_styles[style]} style",
            "Adding final touches"
        ]
        
        for step in steps:
            print(f"- {step}")
            time.sleep(1)
        
        # Simulate cooking time
        cooking_time = random.uniform(3, 5)
        print(f"\nCooking for {cooking_time:.1f} minutes...")
        time.sleep(2)

    def serve_omelet(self, style):
        print(f"\nServing your {style.value} omelet!")
        print("Bon appétit! 🍳")
        
        # Add some fun facts about the omelet style
        facts = {
            OmeletStyle.FRENCH: "Did you know? French omelets are known for their smooth, buttery texture and are often served slightly runny in the center.",
            OmeletStyle.SPANISH: "Fun fact: Spanish omelets (tortilla española) are often served at room temperature and are a popular tapas dish.",
            OmeletStyle.JAPANESE: "Interesting: Japanese omelets (tamagoyaki) are sweet and are often made in a special rectangular pan.",
            OmeletStyle.ITALIAN: "Trivia: Italian frittatas are often served with fresh herbs and are perfect for using up leftover vegetables.",
            OmeletStyle.AMERICAN: "Fun fact: American-style omelets are known for their generous fillings and are often served with toast or hash browns."
        }
        
        print(f"\n{facts[style]}")

    def make_omelet(self, style):
        print(f"\n=== Making a {style.value} Omelet ===")
        self.prepare_ingredients(style)
        self.cook_omelet(style)
        self.serve_omelet(style)

def main():
    cooker = OmeletCooker()
    
    print("Welcome to the International Omelet Cooker!")
    print("Choose an omelet style:")
    
    for i, style in enumerate(OmeletStyle, 1):
        print(f"{i}. {style.value}")
    
    while True:
        try:
            choice = int(input("\nEnter the number of your choice (1-5): "))
            if 1 <= choice <= len(OmeletStyle):
                selected_style = list(OmeletStyle)[choice - 1]
                cooker.make_omelet(selected_style)
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main() 