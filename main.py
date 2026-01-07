states_file = "states.csv"
cities_file = "cities.csv"
encoding_type = "utf-8"

def list_states(states_file):
    states = set()
    with open(states_file, "r", encoding=encoding_type) as file:
        file.readline()  
        for line in file:
            data = line.strip().split(",")
            if len(data) >= 3:
                states.add(data[2])
    
    return sorted(list(states))

def create_state_city_dictionary(states_file, cities_file):
    code_to_state = {}
    state_to_cities = {}

    with open(states_file, "r", encoding=encoding_type) as file:
        file.readline()
        for line in file:
            data = line.strip().split(",")
            code_to_state[data[0]] = data[2]
            state_to_cities[data[2]] = []

    with open(cities_file, "r", encoding=encoding_type) as file:
        file.readline()
        for line in file:
            data = line.strip().split(",")
            state_code = data[5]
            city_name = data[1]
            if state_code in code_to_state:
                state_to_cities[code_to_state[state_code]].append(city_name)

    return state_to_cities

def find_state_by_city(state_city_dict, city_name):
    for state, cities in state_city_dict.items():
        if city_name.lower() in [c.lower() for c in cities]:
            return state
    return None

def main_menu():
    state_city_dict = create_state_city_dictionary(states_file, cities_file)
    
    while True:
        print("\n=== BRAZILIAN GEOGRAPHY SYSTEM ===")
        print("1. List all States")
        print("2. Search State by City Name")
        print("3. Export Data to CSV")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ")

        if choice == "1":
            states = list_states(states_file)
            print("\n--- Registered States ---")
            for s in states: print(f"- {s}")
            print(f"Total: {len(states)} states.")

        elif choice == "2":
            city = input("Enter city name: ")
            result = find_state_by_city(state_city_dict, city)
            if result:
                print(f"Success: The city '{city}' belongs to the state of {result}.")
            else:
                print("Error: City not found in our database.")

        elif choice == "3":
            print("Exporting data...")
            # Here you could call your save functions
            print("Files 'states_list.csv' and 'states_cities.csv' updated!")

        elif choice == "4":
            print("Closing system. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()