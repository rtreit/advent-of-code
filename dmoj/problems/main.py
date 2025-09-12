import sys

NOT_ALIKE_RESULT = "No two snowflakes are alike."
ALIKE_RESULT = "Twin snowflakes found."

def sanitize_snowflake_line(line: str) -> list[int]:
    numbers_in_line = line.split(" ")
    return [int(num) for num in numbers_in_line if num != " "]
    
def solve():
    num_snowflakes = int(sys.stdin.readline().strip())
    all_snowflakes = [sanitize_snowflake_line(sys.stdin.readline().strip()) for _ in range(num_snowflakes)]
    print(all_snowflakes)
    snowflake_sums = [sum(flake) for flake in all_snowflakes]
    print(snowflake_sums)
    if len(snowflake_sums) == len(list(set(snowflake_sums))):
        print(NOT_ALIKE_RESULT)
        return
    # now we know we have at least one set of twins
    # find the index in snowflake_sums of all sums that don't appear only once        
    snowflake_counts = {}
    for snowflake in snowflake_sums:
        if snowflake in snowflake_counts:
            snowflake_counts[snowflake] = snowflake_counts[snowflake] + 1
        else:
            snowflake_counts[snowflake] = 1

    potential_twins = list(set([snowflake for snowflake in snowflake_sums if snowflake_counts[snowflake]> 1]))
    potential_twin_locations = {}
    for index, value in enumerate(snowflake_sums):
        if value in potential_twins:
            if value in potential_twin_locations:
                current_value = potential_twin_locations[value]
                current_value.append(index)
                potential_twin_locations[value] = current_value
            else:
                potential_twin_locations[value] = [index]
    print(potential_twin_locations)
    # now we can work on actually evaluating if the potential twins are the same
    for _, potential_twin in enumerate(potential_twin_locations):
        locations = potential_twin_locations[potential_twin]
        print(all_snowflakes[locations[1]])

def main():
    solve()

if __name__ == "__main__":
    solve()