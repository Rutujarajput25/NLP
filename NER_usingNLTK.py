# ner_nltk.py
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from colorama import Fore, Style, init

# init colorama (for Windows terminal)
init(autoreset=True)

# Ensure required NLTK models are available (downloads only if missing)
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('maxent_ne_chunker', quiet=True)
nltk.download('words', quiet=True)

texts = [
    "Barack Obama was the 44th President of the United States.",
    "Apple is looking at buying a U.K. startup for $1 billion.",
    "Elon Musk founded SpaceX in 2002 in California.",
    "Amazon headquarters is located in Seattle.",
    "The Taj Mahal is in Agra, India.",
    "Cristiano Ronaldo plays for Al Nassr in Saudi Arabia."
]

# Color map (NLTK labels: PERSON, ORGANIZATION, GPE, LOCATION, DATE, MONEY, etc.)
color_map = {
    "PERSON": Fore.GREEN,
    "ORGANIZATION": Fore.CYAN,
    "ORG": Fore.CYAN,
    "GPE": Fore.MAGENTA,
    "LOCATION": Fore.MAGENTA,
    "FACILITY": Fore.MAGENTA,
    "DATE": Fore.RED,
    "MONEY": Fore.YELLOW
}

def extract_entities(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    tree = ne_chunk(tagged, binary=False)
    entities = []
    for subtree in tree:
        # NLTK uses nltk.Tree for named entity chunks
        if hasattr(subtree, "label"):
            label = subtree.label()
            entity = " ".join(token for token, pos in subtree.leaves())
            entities.append((entity, label))
    return entities, tree

if __name__ == "__main__":
    for text in texts:
        print("\n" + text)
        ents, tree = extract_entities(text)
        if not ents:
            print("  (no named entities found)")
        else:
            for ent_text, ent_label in ents:
                color = color_map.get(ent_label, Fore.WHITE)
                print(f"  {color}{ent_text} --> {ent_label}{Style.RESET_ALL}")

        # Optional: print the chunk tree (ASCII) for debugging
        # tree.pretty_print()
