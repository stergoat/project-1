import random

class Game:
    def __init__(self):
        self.rooms = {
            'coral reef': {
                'description': 'You swim into a bright coral reef full of colorful fish.',
                'exits': {'north': 'kelp forest', 'south': 'dark trench'},
                'items': ['magical pearl'],
                'characters': ['seahorse']
            },
            'dark trench': {
                'description': 'You enter the dark trench. It\'s eerie and quiet.',
                'exits': {'north': 'coral reef'},
                'items': [],
                'characters': ['shark']
            },
            'kelp forest': {
                'description': 'You explore the kelp forest, swaying gently with the current.',
                'exits': {'south': 'coral reef'},
                'items': [],
                'characters': []
            }
        }
        self.current_room = 'coral reef'
        self.inventory = []
        self.characters = {
            'seahorse': "The seahorse offers you a magical pearl that will help you on your journey.",
            'shark': "The shark looks very menacing."
        }
        self.puzzle_solved = False

    def print_intro(self):
        print("Welcome to the Ocean!")
        print("You are a wandering fish swimming in the vast ocean.")
        print("Your journey will involve meeting interesting characters and making decisions that will shape your adventure.")
        print("Let's dive in!")

    def look(self):
        room = self.rooms[self.current_room]
        description = room['description']
        items = ', '.join(room['items'])
        characters = ', '.join(room['characters'])
        print(f"{description}\nItems: {items}\nCharacters: {characters}")

    def move(self, direction):
        if direction in self.rooms[self.current_room]['exits']:
            self.current_room = self.rooms[self.current_room]['exits'][direction]
            self.look()
        else:
            print("You can't go that way.")

    def examine(self, item):
        if item in self.rooms[self.current_room]['items']:
            print(f"You see a {item}.")
        else:
            print("There's no such item here.")

    def take(self, item):
        if item in self.rooms[self.current_room]['items']:
            self.inventory.append(item)
            self.rooms[self.current_room]['items'].remove(item)
            print(f"You took the {item}.")
        else:
            print("There's no such item here.")

    def use(self, item):
        if item in self.inventory:
            print(f"You used the {item}.")
            # Implement item use logic if necessary
        else:
            print("You don't have that item.")

    def talk_to(self, character):
        if character in self.characters:
            print(self.characters[character])
        else:
            print("There's no such character here.")

    def give(self, item, character):
        if item in self.inventory and character in self.characters:
            print(f"You gave the {item} to the {character}.")
            self.inventory.remove(item)
            # Implement the logic of giving item if necessary
        else:
            print("You can't give that item to this character.")

    def solve_puzzle(self, answer):
        if not self.puzzle_solved and answer.lower() == "open sesame":
            print("Congratulations! You solved the puzzle.")
            self.puzzle_solved = True
        elif self.puzzle_solved:
            print("You already solved the puzzle.")
        else:
            print("That's not the correct answer.")

    def encounter_npc(self):
        print("\nYou encounter a wise old whale.")
        print("The whale says: 'Hello, young fish. I've seen many things in my time. Would you like to hear a story or ask for advice?'")
        choice = input("Type 'story' to hear a story or 'advice' to ask for advice: ").strip().lower()
        if choice == 'story':
            print("\nThe whale tells you a tale about a hidden treasure in the depths of the ocean...")
            print("It says that many fish have searched for it but only the bravest find it.")
        elif choice == 'advice':
            print("\nThe whale gives you advice: 'Stay away from the dark trenches. They're dangerous and home to mysterious creatures.'")
        else:
            print("\nThe whale looks puzzled and swims away, leaving you to continue your journey.")

    def encounter_shark(self):
        print("\nOh no! You come across a hungry shark!")
        print("The shark looks very menacing.")
        action = input("Type 'fight' to try and fight the shark or 'run' to escape: ").strip().lower()
        if action == 'fight':
            if random.random() > 0.5:
                print("\nYou bravely fight the shark and manage to scare it away. You are victorious!")
            else:
                print("\nThe shark is too strong! You barely escape with your fins intact.")
        elif action == 'run':
            print("\nYou quickly swim away from the shark. That was a close call!")
        else:
            print("\nThe shark grows impatient and decides to leave you alone. Lucky for you!")

    def explore(self):
        print("\nYou decide to explore the ocean further.")
        print("You come across three different paths:")
        print("1. A bright coral reef full of colorful fish.")
        print("2. A dark and mysterious trench.")
        print("3. A serene kelp forest swaying gently with the current.")

        path = input("Which path do you choose? (1, 2, or 3): ").strip()
        if path == '1':
            self.move('north')
        elif path == '2':
            self.move('south')
        elif path == '3':
            self.move('south')
        else:
            print("\nYou can't decide and end up going in circles.")

    def main(self):
        self.print_intro()
        while True:
            self.explore()
            if self.current_room == 'coral reef':
                self.encounter_npc()
            elif self.current_room == 'dark trench':
                self.encounter_shark()
            elif self.current_room == 'kelp forest':
                if 'magical pearl' not in self.inventory:
                    print("\nYou find a small, friendly seahorse.")
                    self.talk_to('seahorse')
                    self.take('magical pearl')
                else:
                    print("\nYou explore the kelp forest but find nothing new.")
            
            continue_game = input("\nDo you want to continue your adventure? (yes/no): ").strip().lower()
            if continue_game != 'yes':
                print("\nThank you for playing the Ocean Adventure! Farewell, brave fish!")
                break

if __name__ == "__main__":
    game = Game()
    game.main()