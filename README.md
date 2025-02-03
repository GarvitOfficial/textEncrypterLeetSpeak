# Leet Speak Converter

## Overview
The **Text Encrypter LEet Speak** is a Python-based text transformation tool that replaces specific letters with symbols, commonly known as "leet speak" or "1337 speak." This script provides a default character substitution scheme while allowing users to define custom mappings for greater flexibility.

## Features
- **Predefined Character Mapping:**  
a → @
e → 3
i → 1
o → 0
s → $
A → @
E → 3
I → 1
O → 0
S → $

- **Custom Mapping Support:** Users can specify their own character replacements.  
- **Command-Line Interface (CLI):** Simple and interactive for easy use.  

## Installation & Execution
### **Prerequisites**
- Python 3.x installed on your system.

### **Execution Steps**
1. Clone or download the repository.
2. Open a terminal or command prompt.
3. Run the script:python main.py
4. Enter the text to be converted.
5. View the default mappings and choose whether to modify them.
6. Receive the transformed output.

## Example Usage
### **Using Default Mappings**
**Input:**  
Enter text to convert: hello world
Do you want to provide custom replacements? (yes/no): no

**Output:**  
Leet Speak Output: h3ll0 w0rld


### **Using Custom Mappings**
**Input:**  
Enter text to convert: hello world
Do you want to provide custom replacements? (yes/no): yes
Enter letters you want to convert (e.g., a:@, e:3, i:1): h:#, l:1, o:*

**Output:**  
Leet Speak Output: #e11* w*r1d


## Future Enhancements
- Predefined leet speak modes (e.g., basic, advanced, hacker-style).
- Ability to save and reuse custom configurations.
- Graphical User Interface (GUI) version for ease of use.

## License
This project is open-source. Feel free to use, modify, and share it as needed.
