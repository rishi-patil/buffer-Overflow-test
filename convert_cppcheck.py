import sys
import json
import xml.etree.ElementTree as ET

def xml_to_json(xml_file, json_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    issues = []
    for error in root.findall("error"):
        issue = {
            "file": error.get("file"),
            "line": error.get("line"),
            "severity": error.get("severity"),
            "message": error.get("msg"),
            "id": error.get("id"),
        }
        issues.append(issue)

    with open(json_file, "w") as f:
        json.dump({"issues": issues}, f, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_cppcheck.py <input.xml> <output.json>")
        sys.exit(1)
    
    xml_to_json(sys.argv[1], sys.argv[2])
