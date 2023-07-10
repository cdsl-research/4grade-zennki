import re

def extract_module(file):
    with open(file, 'r', encoding='utf-8') as f:
        module_dict = {}
        file_lines = f.readlines()

        new_lines = [line.strip() for line in file_lines if line.strip()]
        for i in range(len(new_lines)):
            if new_lines[i] == 'module{':
                j = i + 1
                while new_lines[j] != '}':
                    match = re.search(r'(\w+):\s*(.*)', new_lines[j])
                    if match:
                        if match.group(2) == "":
                            keep = match.group(1)
                            module_dict[keep] = {}
                        else:
                            if keep not in module_dict:
                                module_dict[keep] = {}
                            module_dict[keep][match.group(1)] = match.group(2)
                            module_dict['alive']['ip'] = '192.168.100.143'
                    j += 1
                break
    return module_dict



