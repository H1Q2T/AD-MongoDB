import database

def show_menu():
    while True:
        print("\n--- MongoDB Movie & Series Manager ---")
        print("1. List Titles & Directors")
        print("2. List Titles & Years (Sorted)")
        print("3. Search 'Professor' in Summary")
        print("4. List Titles After 2018")
        print("5. Add New Entry")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            results = database.list_titles_and_directors()
            for item in results:
                print(f"Title: {item.get('title', 'Unknown')}, Director: {item.get('director', 'Unknown')}")

        elif choice == "2":
            results = database.list_titles_and_years_sorted()
            for item in results:
                print(f"Title: {item.get('title', 'Unknown')}, Year: {item.get('year', 'Unknown')}")

        elif choice == "3":
            results = database.search_by_professor()
            if results:
                for item in results:
                    print(f"Title: {item.get('title', 'Unknown')}")
            else:
                print("No results found.")

        elif choice == "4":
            results = database.list_recent_titles()
            for item in results:
                print(f"Title: {item.get('title', 'Unknown')}, Year: {item.get('year', 'Unknown')}, Cast: {', '.join(item.get('cast', []))}")

        elif choice == "5":
            title = input("Enter title: ").strip()
            year = input("Enter year: ").strip()
            director = input("Enter director: ").strip()
            cast = input("Enter cast (comma separated): ").strip()
            summary = input("Enter summary: ").strip()

            if not title or not year or not director or not cast or not summary:
                print("Error: All fields are required.")
            else:
                cast_list = [name.strip() for name in cast.split(",")]
                message = database.add_new_entry(title, year, director, cast_list, summary)
                print(message)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please select a valid option.")

        input("\nPress Enter to return to the menu...")  # Pausa antes de volver al menú

if __name__ == "__main__":
    show_menu()
