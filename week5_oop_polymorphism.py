# week5_oop_polymorphism.py

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def move(self):
        return "🚗 The car is driving smoothly on the road!"

class Plane(Vehicle):
    def move(self):
        return "✈️ The plane is flying high in the sky!"

class Boat(Vehicle):
    def move(self):
        return "⛵ The boat is sailing across the waves!"

class Bicycle(Vehicle):
    def move(self):
        return "🚴 The bicycle is pedaling along the path!"

# main function
def main():
    print("=== Vehicle Movement Simulator ===")
    print("Choose a vehicle to see how it moves:")
    print("1. Car 🚗\n2. Plane ✈️\n3. Boat ⛵\n4. Bicycle 🚴\n")

    try:
        choice = int(input("Enter your choice (1-4): "))
        vehicles = {
            1: Car(),
            2: Plane(),
            3: Boat(),
            4: Bicycle()
        }

        selected_vehicle = vehicles.get(choice)
        if selected_vehicle:
            print("\n" + selected_vehicle.move())
        else:
            print("❌ Invalid choice. Please select between 1-4.")

    except ValueError:
        print("⚠️ Please enter a valid number (1-4).")

if __name__ == "__main__":
    main()
