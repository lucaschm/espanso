import sys

def convert_to_yaml(input_text):
    """
    Converts a comma-separated string into a YAML-formatted list.
    """
    items = [f"  - {item.strip()}" for item in input_text.split(',')]
    return "\n  " + "\n".join(items)

if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #     print("Usage: python comma_to_yaml.py \"comma,separated,values\"")
    #     sys.exit(1)
    
    # input_text = sys.argv[1]
    yaml_output = convert_to_yaml("Electrification, Automation, Digitalization, Innovation, Technology, Engineering, Manufacturing, Artificial Intelligence, Internet of Things, Cybersecurity, Infrastructure, Sustainability, Digital Twin, Metaverse, Transport und Smart Buildings")
    print(yaml_output)