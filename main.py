""""" 
Leet Speak Converter
Author: Slushie
Description: A simple Python script to convert text into leetspeak by replacing specific letters with symbols.
This is just a basic structure and can be extended further.

Default Replacements:
    a -> @
    e -> 3
    i -> 1
    o -> 0
    s -> $
    A -> @
    E -> 3
    I -> 1
    O -> 0
    S -> $
Users can choose to modify these mappings if they wish.
"""

def leet_speak(text: str, replacements: dict) -> str:
    """Convert text into leetspeak by replacing specified characters."""
    return ''.join(replacements.get(char, char) for char in text)

if __name__ == "__main__":
    default_replacements = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$',
                            'A': '@', 'E': '3', 'I': '1', 'O': '0', 'S': '$'}
    
    print("Default replacements:")
    for key, value in default_replacements.items():
        print(f"{key} -> {value}")
    
    user_text = input("Enter text to convert: ")
    use_custom = input("Do you want to provide custom replacements? (yes/no): ").strip().lower()
    
    if use_custom == "yes":
        letters_to_convert = input("Enter letters you want to convert (e.g., a:@, e:3, i:1): ")
        replacements = dict(pair.split(":") for pair in letters_to_convert.split(", "))
    else:
        replacements = default_replacements
    
    print("Leet Speak Output:", leet_speak(user_text, replacements))

