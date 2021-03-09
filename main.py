from core.game import Game

def main():
    game = Game()
    game.printGame()
    
    game.removePair([2,2], [0,0])
    game.deal()
    game.printGame()

if __name__ == "__main__":
    main()
    
