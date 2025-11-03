import random

class BingoGame:
    player_list = []

    def __init__(self):
        self.name = input("Enter your name:")
        self.__random_number = random.randint(0,10)
        self.__guess_left = 3
        self.__win_status = False
        BingoGame.player_list.append(self)

    def check_answer(self):
        try:
            answer = int(input(f"\n{self.name},Please enter your guess:"))
            if answer > self.__random_number:
                print(f"\n{self.name}choose lower number")
            elif answer < self.__random_number:
                print("choose bigger number")
            elif answer == self.__random_number:
                self.__win_status = True
                print("Bingo")
            self.__minus_guess_left()
            print(f"\n{self.__guess_left},guesses left")
        except ValueError:
            print("please enter a valid integer.")
            return

    def __minus_guess_left(self):
        self.__guess_left -= 1 


    def has_guess_left(self):
        return self.__guess_left > 0


    def has_won(self):
        return self.__win_status
    
    @classmethod
    def game_has_winner(cls):
        if any(player.has_won() is True for player in cls.player_list):
            return True
        return False

    @classmethod
    def all_players_out_of_guesses(cls):
        return all(not player.has_guess_left() for player in cls.player_list)



class GameController:
    
    def __init__(self):
        print("building GameContoller object...")
        while True:
            for player in BingoGame.player_list:
                print(player)
                if not player.has_won() and player.has_guess_left():
                    player.check_answer()
            if BingoGame.game_has_winner() or BingoGame.all_players_out_of_guesses():
                break
            # Announce results
        winners = [player.name for player in BingoGame.player_list if player.has_won()]
        if winners:
            print(f"\nGame Over! Winners: {', '.join(winners)}")
        else:
            print("\nGame Over! No winners, all guesses exhausted.")
        

if __name__ == "__main__":
    while True:
        order = input("what do you want to do? (add/start/exit):").lower()
        if order == "add":
            BingoGame()
        elif order == "start":
            if not BingoGame.player_list:
                print("No players added! Please add at least one player.")
            else:
                print("starting")
                GameController()
                break  # Exit after game ends
        elif order == "exit":
            break


