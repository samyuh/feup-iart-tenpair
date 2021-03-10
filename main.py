from core.game import Game, AI
import copy

def main():
    game = Game()
    ai = AI()
    queue = []
    currentOperations = ai.getAllMoves(game.columns, game.rows, game.matrix)

    # State, Operation
    #queue.append(('deal', 'deal'))

    for i in currentOperations:
        gameCopy = copy.deepcopy(game)
        queue.append((gameCopy, i))

    while queue:
        gameState, operation = queue.pop(0)

        if gameState == 'deal':
            print('end')
            break
        else:
            gameState.removePair(operation[0], operation[1])
            gameState.printGame()

            currentOperations = ai.getAllMoves(gameState.columns, gameState.rows, gameState.matrix)
            for i in currentOperations:
                gameCopy = copy.deepcopy(gameState)
                queue.append((gameCopy, i))


if __name__ == "__main__":
    main()

    
