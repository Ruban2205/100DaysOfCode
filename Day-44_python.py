# Create a program to generate random sentences based on templates.
print("\nRuban Gino Singh - Day 44 of the #100DaysOfCode\n")

print("Python program to generate a random sentences based on templates\n")

import random

def generate_sentence():

    templates = [
        "The {noun} {verb} over the {adjective} {noun}.",
        "A {adjective} {noun} {verb} in the {noun}.",
        "The {noun} {adverb} {verb} {preposition} a {adjective} {noun}.",
        "In the {adjective} {noun}, a {noun} {verb} {adverb}."
    ]

    nouns = ["cat", "dog", "bird", "tree", "house"]
    verbs = ["runs", "jumps", "flies", "sings", "swims"]
    adjectives = ["happy", "sad", "colorful", "big", "small"]
    adverbs = ["quickly", "slowly", "loudly", "softly", "boldly"]
    prepositions = ["on", "in", "under", "above", "beside"]

    template = random.choice(templates)

    sentence = template.format(
        noun=random.choice(nouns),
        verb=random.choice(verbs),
        adjective=random.choice(adjectives),
        adverb=random.choice(adverbs),
        preposition=random.choice(prepositions)
    )

    return sentence

print(generate_sentence())

# --------------------------------------------------------- #