import file_reader
import debug_file_paths
import adding_data

def main():
    print("Wellcome to Puzzles")
    name = input("What is your name? ")
    print(f"Hello {name.capitalize()}!")

    while True:
        user_choice = input("\nFirst let's debug to check for all the files\n01. Ok let's Debug\n02. No I want to start playing\nEnter your choice : ")
        if user_choice.lower() in ["01","1","yes"]:
            result = debug_file_paths.debug_paths()
            if not result == "ok":
                print("Now we'll add the data.\nAs they are not found in the program.")
                adding_data.run()
            print(f"Best of Luck {name.capitalize()}!\n")
            break
        elif user_choice.lower() in ["02","2","no"]:
            print(f"Ok\nBut I can't be sure the Game will work\nBest of Luck {name.capitalize()}!")
            break
        else:
            print("Please enter a valid choice.\n1 or 2 or yes or no")

main()