import threading
from datetime import datetime

class Animal:
    def __init__(self, name):
        """Initialize an Animal with a name."""
        self.name = name

    def move(self):
        """Base move method to be overridden."""
        return f"{self.name} is moving."

    def save_action(self, filename, event):
        """Save animal's move action to a file, waiting for file creation."""
        event.wait()
        try:
            with open(filename, "a") as file:
                file.write(f"{self.move()} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S EAT')}\n")
            print(f"Saved {self.name}'s action to '{filename}'.")
        except PermissionError:
            print(f"Error: Permission denied when writing to '{filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

class Dog(Animal):
    def move(self):
        """Override move for Dog (polymorphism)."""
        return f"{self.name} is swinging its tail"

class Bird(Animal):
    def move(self):
        """Override move for Bird (polymorphism)."""
        return f"{self.name} is flapping its wings 🐦"

def create_action_file(filename, event):
    """Create an empty file for animal actions."""
    try:
        with open(filename, "w") as file:
            file.write(f"Animal Actions Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S EAT')}\n")
        print(f"Created '{filename}' successfully.")
        event.set()
    except PermissionError:
        print(f"Error: Permission denied when creating '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def main():
    # Create instances
    dog = Dog("MAX")
    bird = Bird("KASUKU")
    action_file = "animal_actions.txt"
    file_created_event = threading.Event()

    # Display move actions
    print("Dog Action:", dog.move())
    print("Bird Action:", bird.move())

    # Create threads for file creation and animal actions
    create_thread = threading.Thread(target=create_action_file, args=(action_file, file_created_event))
    dog_thread = threading.Thread(target=dog.save_action, args=(action_file, file_created_event))
    bird_thread = threading.Thread(target=bird.save_action, args=(action_file, file_created_event))

    # Start threads
    create_thread.start()
    dog_thread.start()
    bird_thread.start()

    # Wait for completion
    create_thread.join()
    dog_thread.join()
    bird_thread.join()

    print("Program execution completed.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")