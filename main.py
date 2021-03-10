from core.game import Game, AI

def main():
    game = Game()
    ai = AI()
    ai.getAllMoves(game.columns, game.rows, game.matrix)


    game.printGame()
    # Pair -> [row, column] -> [y, x]
    game.removePair([3,8], [2,8])
    game.removePair([2,2], [0,0])
    game.removePair([1,0], [0,0])

    game.deal()
    game.printGame()

    game.removePair([3,8], [2,8])
    game.printGame()

    game.deal()
    game.printGame()

if __name__ == "__main__":
    main()

    
