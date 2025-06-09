import yaml
import json

def load_yaml(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def convert_to_onix(data):
    # Example conversion to ONIX format
    onix_data = f"""<?xml version="1.0" encoding="UTF-8"?>
<ONIXMessage>
    <Header>
        <Sender>
            <SenderName>{data.get('publisher', 'Unknown Publisher')}</SenderName>
        </Sender>
    </Header>
    <Product>
        <Title>{data.get('title', 'Untitled')}</Title>
        <Author>{data.get('author', 'Unknown Author')}</Author>
        <ISBN>{data.get('isbn', 'N/A')}</ISBN>
        <Description>{data.get('description', 'No description available.')}</Description>
    </Product>
</ONIXMessage>
"""
    return onix_data

def convert_to_schema(data):
    # Example conversion to Schema.org format
    schema_data = {
        "@context": "https://schema.org",
        "@type": "Book",
        "name": data.get('title', 'Untitled'),
        "author": data.get('author', 'Unknown Author'),
        "isbn": data.get('isbn', 'N/A'),
        "description": data.get('description', 'No description available.'),
        "publisher": data.get('publisher', 'Unknown Publisher')
    }
    return json.dumps(schema_data, indent=4)

def save_to_file(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)

if __name__ == "__main__":
    yaml_file = 'Camille du Gast_metadata.yaml'  # Replace with your YAML file path
    onix_file = 'Camille du Gast_output.onix'  # Desired output ONIX file path
    schema_file = 'Camille du Gast_output.json'  # Desired output Schema.org file path

    # Load YAML data
    yaml_data = load_yaml(yaml_file)

    # Convert to ONIX and Schema.org formats
    onix_data = convert_to_onix(yaml_data)
    schema_data = convert_to_schema(yaml_data)

    # Save the converted data to files
    save_to_file(onix_data, onix_file)
    save_to_file(schema_data, schema_file)

    print(f"ONIX data saved to {onix_file}")
    print(f"Schema.org data saved to {schema_file}")
