import random

class VacuumCleaner:
    def __init__(self, location, environment):
        self.location = location
        self.environment = environment

    def sense(self):
        return self.environment[self.location]

    def move(self, new_location):
        self.location = new_location
        print(f"Moving to {new_location}")

    def clean(self):
        if self.sense() == 1:
            print("Cleaning dirt")
            self.environment[self.location] = 0
        else:
            print("No dirt to clean")

def random_environment(size):
    return [random.choice([0, 1]) for _ in range(size)]

def main():
    room_size = 5
    environment = random_environment(room_size)

    vacuum_cleaner = VacuumCleaner(location=random.randint(0, room_size - 1), environment=environment)

    print("Initial environment:", environment)

    for _ in range(room_size):
        vacuum_cleaner.clean()
        new_location = random.randint(0, room_size - 1)
        vacuum_cleaner.move(new_location)
        print("Current environment:", vacuum_cleaner.environment)
        print()

if __name__ == "__main__":
    main()
