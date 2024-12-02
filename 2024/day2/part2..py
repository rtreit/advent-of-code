with open ("./input.txt", "r") as file:
    data = file.read().split("\n")

def is_safe_report(report):
    """
    each level differs by at least one and at most three
    levels are all increasing or decreasing
    """
    # start at the beginning
    pointer = 0
    # determine if we're increasing or decreasing 
    # 1 increasing
    # -1 decreasing
    if report[0] - report[1] == 0:
        # if we're not increasing or decreasing its not safe
        return False
    elif report[0] > report[1]:
        direction = -1
    else:
        direction = 1
    while pointer < len(report)-1:
        item = report[pointer]
        next_item = report[pointer + 1]
        if (abs(item - next_item) < 1 or abs(item-next_item)> 3):
            return False
        if direction == 1:
            if (item == next_item) or (next_item < item):
                return False
        if direction == -1:
            if (item == next_item) or (next_item > item):
                return False            
        pointer += 1
    return True

def dampen_unsafe_report(report):
    """
    if removing a single level makes an unsafe report safe, consider it safe
    """
    for i, _ in enumerate(report):
        report_copy = report.copy()
        report_copy.pop(i)
        if is_safe_report(report_copy):
            return True
    return False

reports = []
for raw_row in data:
    parsed_reports = []
    report_values = raw_row.split(" ")
    for value in report_values:
        converted_value = int(value)
        parsed_reports.append(converted_value)
    reports.append(parsed_reports)

safe_reports = []
unsafe_reports = []
[safe_reports.append(report) if is_safe_report(report) else None for report in reports]
[unsafe_reports.append(report) if report not in safe_reports else None for report in reports]

dampened_reports = []
for report in unsafe_reports:
    if dampen_unsafe_report(report):
        dampened_reports.append(report)

print(f"Part 2: {len(safe_reports) + len(dampened_reports)}")