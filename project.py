import sys
import os
import json
import yaml
import xml.etree.ElementTree as ET

def load_json(filepath):
    # Task 2
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    # Task 3
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_yaml(filepath):
    # Task 4
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def save_yaml(data, filepath):
    # Task 5
    with open(filepath, 'w', encoding='utf-8') as f:
        yaml.safe_dump(data, f, allow_unicode=True)

def load_xml(filepath):
    # Task 6
    tree = ET.parse(filepath)
    root = tree.getroot()
    
    data = {}
    for child in root:
        data[child.tag] = child.text
    return data

def save_xml(data, filepath):
    # Task 7
    root = ET.Element("root")
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    tree.write(filepath, encoding='utf-8', xml_declaration=True)

def main():
    # Task 1
    if len(sys.argv) != 3:
        print("Sposób użycia: program.exe pathFile1.x pathFile2.y")
        print("Formaty: .json, .yml, .yaml, .xml")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(input_file):
        print(f"Błąd: Plik wejściowy {input_file} nie istnieje.")
        sys.exit(1)
        
    in_ext = os.path.splitext(input_file)[1].lower()
    out_ext = os.path.splitext(output_file)[1].lower()
    
    try:
        if in_ext == '.json':
            data = load_json(input_file)
        elif in_ext in ['.yml', '.yaml']:
            data = load_yaml(input_file)
        elif in_ext == '.xml':
            data = load_xml(input_file)
        else:
            print("Nieobsługiwany format pliku wejściowego.")
            sys.exit(1)
    except Exception as e:
        print(f"Błąd podczas parsowania pliku wejściowego: {e}")
        sys.exit(1)

    try:
        if out_ext == '.json':
            save_json(data, output_file)
        elif out_ext in ['.yml', '.yaml']:
            save_yaml(data, output_file)
        elif out_ext == '.xml':
            save_xml(data, output_file)
        else:
            print("Nieobsługiwany format pliku wyjściowego.")
            sys.exit(1)
        print(f"Przekonwertowano {input_file} do {output_file}")
    except Exception as e:
        print(f"Błąd podczas zapisu pliku wyjściowego: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()