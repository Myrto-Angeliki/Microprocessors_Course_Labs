class Menu():
    def __init__(self, menu_options=[]):
        self.menu_options = menu_options

    def handle_menu_option(self, option):
        pass

    def display_menu(self):
        pass

    def prompt_input(self):
        print("\n Choose an option:", end=" ")
        option = input().strip()
        while option not in self.menu_options:
            print(f" Please choose an option between 1 and {self.menu_options[-1]}:", end=" ")
            option = input().strip()
        print()
        return option

    def start_menu(self):
        self.display_menu()
        option = self.prompt_input()
        while option != self.menu_options[-1]:
            self.handle_menu_option(option)
            self.display_menu()
            option = self.prompt_input()

    def set_menu_options(self, menu_opts):
        self.menu_options = menu_opts

    def get_menu_options(self):
        return self.menu_options