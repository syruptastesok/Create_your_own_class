# Surya Marimuthu
# 10.1: Create your own class
# Resources used: Lecture notes and I used https://www.geeksforgeeks.org/getter-and-setter-in-python/ for the get-set methods

# class
class Game:

    # class variable
    best_games = ["Red Dead Redemption 2", "Spider-man", "God of War", "Last of Us", "Uncharted 2", "Super Smash Bros.", "Pokemon HeartGold"]

    # defining the init variable
    def __init__(self, title, console, price,):
        # private data variables
        self.__title = title
        self.__price = price
        self.__console = console

    # first method: rates the inputted console and rates it out of 10
    def console_rating(self, console):
        self.__console = console
        # since there is only one 10/10 console if it is PS4 return 10/10
        if self.__console == "PS4":
            return (f"10/10 console. We are best friends now. Good job on choosing {console}.")
        # if the console is PS3, return 8/10
        elif self.__console == "PS3":
            return (f"8/10 game. {console} is a solid choice")
        # any other console will be a 5/10
        else:
            return ("5/10. There's a whole world of better consoles out there :(")

    # second method: rates the inputted video game and rates it out of 10
    def title_rating(self, title):
        # if the inputted title is in the class variable, best_games, return 10/10
        if self.__title in self.best_games:
            return (f"10/10. We are best friends now. {title} is a fantastic choice")
        # if it's not in the best_games list then return 5/10
        else:
            return (f"5/10. We can be aquitances, but not best friends. Sorry, {title} is not a great game")
    
    # third method: rates the inputted price and rates it out of 10
    def price_rating(self, price):
        # converting price to integer
        self.__price = int(price)
        # checks if the price is less than 0 which is not possible
        if self.__price < 0:
            return ("Hey, the price can't be negative!")
        # if price is less than 30 return message
        elif self.__price < 30:
            return ("I respect it, money doesn't grow on trees")
        # if the price is less than or equal to 60 return message
        elif self.__price <= 60: 
            return ("Hey, I get it new games tend to cost a lot.")
        # any other price will be greater than 60 so return this messsage
        else:
            return ("Wow, that's a lot of money to spend on a game, but I respect it. Some games are worth the money.")

    # first set method
    def set_title(self, title):
        self.__title = title

    # second set method
    def set_price(self, price):
        # int casting price
        self.__price = int(price)

    # third set method
    def set_console(self, console):
        self.__console = console

    # first get method
    def get_title(self, title):
        return self.__title

    # second get method
    def get_price(self, price):
        return self.__price

    # third get method
    def get_console(self, console):
        return self.__console

# demo program
def main():
    # greeting the user
    # demo program will basically ask the user to input their favorite video game, console, and their average price range when buying games
    # and then will judge them based on their choices 
    print("Hello! Today I will be judging you!")
    # asking user to input their favorite game
    title = input("Please input your favorite video game: ")
    # asking user to input their favorite console
    console = input("Please input your favorite console: ")   
    # continues this loop until there is a valid input
    while True:    
        try:
            # asking user to input their average price they pay for new games
            price = input("On average, how much do you pay for new games? (Please don't include the $ sign): ")
            # tries to convert price to a float
            price = float(price)
            # if successful break        
            break
        # if not display error message
        except ValueError:
            print("Invalid price. Please try again")
            
    # inputting the arguemnts into the init method
    video_game = Game(title, console, price)
    # while True loop so it continues instead of ending after one command is inputted
    while True:
        # giving the user the options for their commands
        command1 = input("Please choose a command for what I will rate first. Your options are title, console, price, display, or exit: ")
        # if the command is title, rate their video game using the title_rating method
        if command1 == "title":
            print(video_game.title_rating(title))
        # if the command is console, rate their console using the console_rating method
        elif command1 == "console":
            print(video_game.console_rating(console))
        # if the command is price, rate their price using the price_rating method
        elif command1 == "price":
            print(video_game.price_rating(price))
        # if the command is price, display the user's previously inputted responses using the get-set methods
        elif command1 == "display":
            print("Here you can see what your previous responses were")
            # using the set_title method to set their title as their previous respose
            video_game.set_title(title)
            # using the set_console method to set their console as their previous response
            video_game.set_console(console)
            # using the set_price method to set their price as their previous response
            video_game.set_price(price)
            # giving the user their inputted video game using the get_title method
            print(f"The game you chose was {video_game.get_title(title)} ")
            # giving the user their inputted console using the get_console method
            print(f"The console you chose was {video_game.get_console(console)}")
            # giving the user their inputted price using the get_price method
            print(f"The average price you pay for new games is ${video_game.get_price(price)}")
        # if the command is exit display ending message and end the program
        elif command1 == "exit":
            print("Goodbye!")
            break
        # if there is any other command inputted, print error message
        else:
            print("Invalid command. Please try again.")
    



if __name__ == "__main__":
    main()

