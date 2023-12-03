# Day 2 Part 1
import pandas as pd
with open("day2/input.txt") as f:
    data = f.readlines()
df = pd.DataFrame(columns=["Id", "Red", "Blue", "Green"])
for line in data:
    id = int(line.split(":")[0].split(" ")[1])
    rounds = line.split(":")[1].split(";")
    max_red = 0
    max_blue = 0
    max_green = 0
    for round in rounds:
        draw = round.split(",")
        for color in draw:
            color_split = color.lstrip().split(" ")
            num_color = int(color_split[0])
            type_color = color_split[1].replace("\n", "")
            if type_color == "red":
                if num_color > max_red:
                    max_red = num_color
            elif type_color == "green":
                if num_color > max_green:
                    max_green = num_color
            elif type_color == "blue":
                if num_color > max_blue:
                    max_blue = num_color               
    new_df  = pd.DataFrame({"Id": [id], "Red": [max_red], "Blue": [max_blue], "Green": [max_green]})
    df = pd.concat([df, new_df])
df = df.reset_index(drop=True)
red_limit = 12
green_limit = 13
blue_limit = 14
red_game_match = df["Red"] <= red_limit
green_game_match = df["Green"] <= green_limit
blue_game_match = df["Blue"] <= blue_limit
print(df[red_game_match & green_game_match & blue_game_match].Id.sum())