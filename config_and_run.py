from condition_rule import extract_rule
from module_ana import extract_module
from pod_status.cpu_and_memori import calculate_metrics_percentage
import time

def extract_condition_code(file_path):
    with open(file_path, 'r', encoding='UTF-8') as file:
        code = file.read()

    condition_start = code.find("condition{") + len("condition{")
    condition_end = code.find("}", condition_start)

    condition_code = code[condition_start:condition_end].strip()
    return condition_code

def convert_condition_code(condition_code):
    converted_code = condition_code.replace("condition{", "").replace("}", "").strip()
    return converted_code

# 条件コードをファイルから抽出
file_path = 'test6.mtr'  # 実際のファイルパスに適切な値を設定してください
condition_code = extract_condition_code(file_path)

# 条件コードを変換
converted_code = convert_condition_code(condition_code)

Extract_rule = extract_rule(file_path)
module = extract_module(file_path)

if "infinite_loop = True:" in converted_code:
    while True:
        if "cpu_pod" in converted_code:
            cpu = calculate_metrics_percentage("test.json")
            w, p = int(cpu[0][2]), int(cpu[1][2])
            print(w,p)
            # if w >= 80 or p >= 80:
            #     print("異状")
            # else:
            #     print("正常")
            
            time.sleep(10)
            
