import yaml
# subprocess serve per andare a richiamare Pandoc
import subprocess

# Carica i metadati YAML
def load_metadata(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

# Funzione per eseguire la conversione con Pandoc
def convert_with_pandoc(input_files, output_file, metadata, pdf_engine=None):
    command = [
        'pandoc', *input_files,  # Passa tutti i file di input
        '--metadata-file', metadata,
        '--output', output_file
    ]
    
    # Gestisci la conversione in PDF con un motore specificato (opzionale)
    if pdf_engine:
        command.extend(['--pdf-engine', pdf_engine])

    # Esegui il comando Pandoc
    subprocess.run(command, check=True)
    print(f"Generato: {output_file}")

# Main script
def main():
    yaml_file = 'metadati.yaml'  # Il file YAML contenente i metadati
    metadata = load_metadata(yaml_file)  # Carica i metadati
    
    # Estrai i file di input e i formati di output
    input_files = metadata.get('gestione_documentale', {}).get('input_files', [])
    output_formats = metadata.get('gestione_documentale', {}).get('output_formats', [])

    if not input_files:
        print("Nessun file di input specificato nel file YAML.")
        return

    # Ciclo su tutti i formati di output richiesti
    for format in output_formats:
        if format == 'pdf':
            output_file = 'Sport900.pdf'
            convert_with_pandoc(input_files, output_file, yaml_file, pdf_engine="xelatex")
        elif format == 'html':
            output_file = 'Sport900.html'
            convert_with_pandoc(input_files, output_file, yaml_file)
        elif format == 'epub':
            output_file = 'Sport900.epub'
            convert_with_pandoc(input_files, output_file, yaml_file)

if __name__ == "__main__":
    main()