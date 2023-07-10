import json
import time
start_time = time.time()
def calculate_percentage(value, max_value):
    percentage = round((value / max_value) * 100)
    return str(percentage)

def calculate_metrics_percentage(file):
    with open(file, 'r', encoding='UTF-8') as json_file:
        data = json.load(json_file)
        pod_metrics = data["pod_metrics"]

        # メモリとCPU使用率をパーセンテージに変換する
        max_memory = 2871680  # メモリの最大値
        max_cpu = 100000  # CPUの最大値

        for metrics in pod_metrics:
            if len(metrics) >= 3:
                memory = int(metrics[1])
                cpu = int(metrics[2])
                metrics[1] = calculate_percentage(memory, max_memory)
                metrics[2] = calculate_percentage(cpu, max_cpu)
                metrics.append(calculate_percentage(cpu, max_cpu))  # CPU使用率を追加

        return pod_metrics

# ファイルパスを指定して結果を受け取る
file_path = "C:/Users/admin/Desktop/研究/4kennkyuu/test.json"
result = calculate_metrics_percentage(file_path)

# 結果を表示する
formatted_result = [[pod[0], pod[1], pod[2]] for pod in result]# メモリとCPU使用率のみ表示
print(formatted_result)
end_time = time.time() - start_time
print(end_time)

