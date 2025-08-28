from datetime import datetime

class Smartphone:
    def __init__(self, brand, model, storage):
        """Initialize a Smartphone with brand, model, and storage."""
        self._brand = brand  # Protected attribute
        self._model = model
        self.__storage = storage  # Private attribute (encapsulation)
        self._creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S EAT")  # Timestamp

    def get_storage(self):
        """Public method to access private __storage (encapsulation)."""
        return self.__storage

    def save_details(self, filename):
        """Save smartphone details to a text file."""
        details = (
            f"Brand: {self._brand}\n"
            f"Model: {self._model}\n"
            f"Storage: {self.__storage}GB\n"
            f"Created: {self._creation_time}\n"
        )
        try:
            with open(filename, "w") as file:
                file.write(details)
            print(f"Saved smartphone details to '{filename}'.")
        except PermissionError:
            print(f"Error: Permission denied when writing to '{filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

    def display_info(self):
        """Display smartphone details."""
        return f"{self._brand} {self._model}, {self.__storage}GB"

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        """Initialize a GamingSmartphone with additional cooling_system."""
        super().__init__(brand, model, storage)
        self._cooling_system = cooling_system

    def display_info(self):
        """Override display_info to include cooling system (polymorphism)."""
        return f"{self._brand} {self._model} (Gaming), {self.get_storage()}GB, Cooling: {self._cooling_system}"

def main():
    # Create instances
    phone = Smartphone("Samsung", "Galaxy S23", 128)
    gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 256, "Liquid Cooling")

    # Display information
    print("Smartphone Info:", phone.display_info())
    print("Gaming Smartphone Info:", gaming_phone.display_info())

    # Save to files
    phone.save_details("smartphone.txt")
    gaming_phone.save_details("gaming_smartphone.txt")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")