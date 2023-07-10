import re

def extract_module_conditions(text):
    module_conditions = re.findall(r"(\w+)\s*{\n\s*loop\(3,3s\)\n\s*(.+?)\n\s*}", text, re.DOTALL)
    conditions = {}

    for module, condition_text in module_conditions:
        lines = condition_text.strip().split("\n")
        loop_condition = "loop(3,3s)"
        comparison = ""

        for line in lines:
            line = line.strip()
            if line.startswith("loop"):
                loop_condition = line
            elif line.endswith(":"):
                comparison = line.rstrip(":")
        
        condition = {
            "loop_condition": loop_condition,
            "comparison": comparison
        }
        conditions[module] = condition
    
    return conditions

def extract_rule(file_path):
    with open(file_path, "r", encoding="UTF-8") as file:
        text = file.read()
    
    module_conditions = extract_module_conditions(text)

    return module_conditions

# モジュールの条件を抽出して辞書型に変換

