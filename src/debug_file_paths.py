import os
import csv

def debug_paths():
    output = ""
    print("=== DEBUGGING FILE PATHS ===")

    # 1. Show current working directory
    cwd = os.getcwd()
    print(f"1. Current Working Directory: {cwd}")

    # 2. Show script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"2. Script Directory (src folder): {script_dir}")

    # 3. Show parent directory
    parent_dir = os.path.dirname(script_dir)
    print(f"3. Parent Directory (project root): {parent_dir}")

    # 4. Show what should be the data folder path
    data_dir_attempt1 = os.path.join(parent_dir, "data")
    print(f"4. Data Directory Attempt 1: {data_dir_attempt1}")

    # 5. Alternative: relative from script
    data_dir_attempt2 = os.path.join(script_dir, "..", "data")
    data_dir_attempt2 = os.path.normpath(data_dir_attempt2)
    print(f"5. Data Directory Attempt 2: {data_dir_attempt2}")

    # 6. Check if data folder exists
    print(f"\n6. Checking if data folder exists:")
    print(f"   Attempt 1 exists: {os.path.exists(data_dir_attempt1)}")
    print(f"   Attempt 2 exists: {os.path.exists(data_dir_attempt2)}")

    # 7. List files in data folder if it exists
    if os.path.exists(data_dir_attempt1):
        print(f"\n7. Files in {data_dir_attempt1}:")
        for file in os.listdir(data_dir_attempt1):
            print(f"   - {file}")
            output = "ok"
    elif os.path.exists(data_dir_attempt2):
        print(f"\n7. Files in {data_dir_attempt2}:")
        for file in os.listdir(data_dir_attempt2):
            print(f"   - {file}")
            output = "ok"
    else:
        print("\n7. Data folder not found in either location!")

        # Try to find data folder anywhere
        print("\nSearching for data folder...")
        for root, dirs, files in os.walk(parent_dir):
            if "data" in dirs:
                print(f"Found 'data' folder at: {os.path.join(root, 'data')}")
                actual_data_dir = os.path.join(root, "data")
                print(f"Files in actual data folder:")
                for file in os.listdir(actual_data_dir):
                    print(f"   - {file}")
                break
            else:
                output = "not ok"
                break
    return output