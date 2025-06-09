import re

def modify_markdown(file_path, output_path, rules):
    """
    Modifica un file Markdown in base a espressioni regolari definite dall'utente.
    
    :param file_path: Percorso al file Markdown da modificare.
    :param output_path: Percorso per salvare il file modificato.
    :param rules: Lista di dizionari con le regole di modifica. Ogni regola deve avere:
                  - "pattern": L'espressione regolare da cercare.
                  - "replace": Il contenuto con cui sostituire il pattern (o None per rimuoverlo).
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    for rule in rules:
        pattern = rule.get("pattern")
        replace = rule.get("replace")
        content = re.sub(pattern, replace, content)
    
 
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"File modificato salvato in '{output_path}'.")

# Regole di esempio
rules = [
    {
           "pattern": r"\[[^]]*\]",  # Rimuovere contenuto dentro le parentesi quadre
        "replace": ""  # Vuoto per rimuoverlo
    },
    # Rimuovere contenuto dentro le parentesi
    {
        "pattern": r"\([^)]*\)",  # Rimuovere contenuto dentro le parentesi
        "replace": ""  # Vuoto per rimuoverlo
    },
    # Rimuovere sequenze come {#...}
    {
        "pattern": r"\{[^}]*\}",  # Sequenza da rimuovere
        "replace": ""  # Vuoto per rimuoverlo
    },
    # Rimuovere sidebar e simili
    {
        "pattern": r"::::.*?::::\n?",  # Rimuovere blocchi come :::: ... ::::
        "replace": ""  # Vuoto per rimuoverlo
    },
    {
        "pattern": r"\s*\]\s*",  # Rimuovere chiusure di parentesi quadre
        "replace": ""  # Vuoto per rimuoverlo
    },
    {
        "pattern": r"\s*\)\s*",  # Rimuovere chiusure di parentesi tonde
        "replace": ""  # Vuoto per rimuoverlo
    }
]

# Percorsi ai file
input_file = "index.md"   # File Markdown di input
output_file = "index(modificato).md" # File Markdown modificato

# Esecuzione dello script
modify_markdown(input_file, output_file, rules)
