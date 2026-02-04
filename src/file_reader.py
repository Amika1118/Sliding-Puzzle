import csv
import os
import random
import logging

location = {"x":[], "y":[]}
puzzle  =  {"x":[], "y":[]}


def read_wining_locations(file_number):
    try:
        # Open the winning locations CSV file
        with open("../data/winning_locations.csv", "r", newline="") as csvfile:
            # Create the location name string (e.g., "location_01")
            file = f"location_0{file_number}"

            # Create CSV reader and skip the header row
            reader = csv.reader(csvfile)
            next(reader)

            # Search for the specific location in the file
            for row in reader:
                # Check if this row matches the requested location
                if row[0] == file:
                    # Extract x coordinates (rows) - take every other column starting from index 2
                    location["x"].append(row[2::2])  # Gets: tile1_row, tile2_row, tile3_row, etc.

                    # Extract y coordinates (columns) - take every other column starting from index 3
                    location["y"].append(row[3::2])  # Gets: tile1_col, tile2_col, tile3_col, etc.
    except FileNotFoundError:
        print("Please Run the Debug File first.\nAnd Run the Game again")
    # Return the location dictionary containing x and y coordinate lists
    return location

def read_puzzle(difficulty, file_number):
    file_path = f"../data/variations_location_0{file_number}.csv"

    # First pass: collect puzzle numbers
    puzzle_numbers = []
    with open(file_path, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header

        for row in reader:
            if row[1] == difficulty.capitalize():
                # Extract number from "location_01_puzzle_01" -> "01"
                number = int(row[0][-2:])  # Get last 2 characters
                puzzle_numbers.append(number)

    if not puzzle_numbers:
        print(f"No puzzles found for difficulty: {difficulty}")
        return None

    random.shuffle(puzzle_numbers)
    chosen_number = puzzle_numbers[0]

    # Second pass: find the chosen puzzle
    with open(file_path, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header

        for row in reader:
            if row[1] == difficulty.capitalize():
                # Extract number from "location_01_puzzle_01" -> "01"
                number = int(row[0][-2:])

                if number == chosen_number:

                    # Extract x and y coordinates correctly
                    # Columns: 0=puzzle_id, 1=difficulty, 2=estimated_moves
                    # Then tile1_row(3), tile1_col(4), tile2_row(5), tile2_col(6), etc.
                    # empty_row(-2), empty_col(-1)

                    # For tiles 1-8 (columns 3 to 18)
                    for i in range(3, 19, 2):  # Step by 2 for row,col pairs
                        puzzle["x"].append(int(row[i]))  # row
                        puzzle["y"].append(int(row[i + 1]))  # col

                        print(row[i])
                        print(row[i + 1])

                    # Add empty tile (0) - last two columns
                    puzzle["x"].append(int(row[-2]))  # empty_row
                    puzzle["y"].append(int(row[-1]))  # empty_col

                    print(row[-2])
                    print(row[-1])

                    break

    return puzzle

