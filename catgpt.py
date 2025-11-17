
---

# 🐍 **catgpt.py**

```python
import json
import random
import argparse
import os

MODEL_PATH = os.path.join("models", "cat_brain.json")

def load_model():
    with open(MODEL_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_cat_response(prompt, model, mood=None):
    """
    Generiert eine absurde Katzenantwort.
    """
    base_response = random.choice(model["responses"])

    if mood and mood in model["moods"]:
        mood_modifier = random.choice(model["moods"][mood])
        return f"{base_response} {mood_modifier}"

    # 10% Chance, einfach zufällig ein Objekt vom Tisch zu werfen
    if random.random() < 0.1:
        return "*wirft ein Glas vom Tisch*"

    return base_response

def main():
    parser = argparse.ArgumentParser(description="CatGPT – das schlechteste KI-Modell der Welt.")
    parser.add_argument("prompt", type=str, help="Benutzereingabe")
    parser.add_argument("--mood", type=str, help="Stimmung der Katze", choices=["hungry", "sleepy", "chaotic"])
    args = parser.parse_args()

    model = load_model()
    response = generate_cat_response(args.prompt, model, mood=args.mood)

    print(f"😺 CatGPT: {response}")

if __name__ == "__main__":
    main()
