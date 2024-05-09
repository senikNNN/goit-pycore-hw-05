from sys import argv
from re import split

def parse_log_line(line: str) -> dict:
    pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) ([\w .%]+)"
    line = split(pattern, line.strip())
    return {"date": line[1], "time": line[2], "level": line[3], "info": line[4]}


def load_logs(file_path: str) -> list:
    logs = list()
    with open(file_path, 'r') as log_file:
        for log_line in log_file:
            logs.append(parse_log_line(log_line))
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = list()
    for log in logs:
        if log["level"] == level:
            filtered_logs.append(log)
    return filtered_logs

def count_logs_by_level(logs: list) -> dict:
    counted_logs = dict()
    for log in logs:
        if log['level'] in counted_logs:
            counted_logs[log['level']] += 1
        else:
            counted_logs[log['level']] = 1
    return counted_logs

def display_log_counts(counts: dict):
    for element in counts:
        print(f"У рівні логування: {element} \tКількість: {counts[element]}")

def display_chosen_log(logs: list, level: str):
    if level:
            filtered_logs = filter_logs_by_level(logs, level)
            for log in filtered_logs:
                print(f"{log["date"]} {log["time"]} {log["level"]} {log["info"]}")

def  main():
    try:
        path = argv[1]
        if len(argv) > 2:
            serch_level = argv[2]
        else:
            serch_level = None

        data = load_logs(path)
        display_log_counts(count_logs_by_level(data))
        display_chosen_log(data, serch_level)
    except FileNotFoundError:
        print("Log file not found!")
    except IndexError:
        print("Incorrect format of the log file!")
    except Exception as e:
        print("an indefinite exception:\n" + e)


if __name__ == "__main__":
    main()


