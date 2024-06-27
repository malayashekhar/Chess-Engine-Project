
"""
Designing the main game framework.
Handling user input.
Coding the game and applying various algorithms for each move.

"""


import chessEngine


class Game:

    def __init__(self, p, screen, clock, MAX_FPS, DIMENSION, SQ_SIZE, IMAGES):
        self.p = p
        self.screen = screen
        self.clock = clock
        self.MAX_FPS = MAX_FPS
        self.DIMENSION = DIMENSION
        self.SQ_SIZE = SQ_SIZE
        self.IMAGES = IMAGES

    def main0(self):

        # Init. Variables
        gs = chessEngine.GameState()
        running = True
        validMoves = gs.getValidMoves()
        moveMade = False  # flag variable for when a move is made
        animate = False  # flag variable for when we should animate a move
        sqSelected = ()  # no sq is selected, keep track of the last user (tuple: row, col)
        playerClicks = []  # keep track of player clicks (two tuples [(old, old), (new, new)])
        GameOver = False

        ''' Start Engine '''

        while running:

            for e in self.p.event.get():
                if e.type == self.p.QUIT:
                    running = False

                # Mouse handlers
                elif e.type == self.p.MOUSEBUTTONDOWN:
                    if not GameOver:
                        location = self.p.mouse.get_pos()  # gets the x,y coordinate
                        col = location[0] // self.SQ_SIZE
                        row = location[1] // self.SQ_SIZE

                        # if the player clicks the square twice (undo action)
                        if sqSelected == (row, col):
                            sqSelected = ()
                            playerClicks = []

                        # else
                        else:
                            sqSelected = (row, col)
                            playerClicks.append(sqSelected)

                        # the change of pieces
                        if len(playerClicks) == 2:
                            move = chessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                            for i in range(len(validMoves)):
                                if move == validMoves[i]:
                                    gs.makeMove(move)
                                    moveMade = True
                                    animate = True
                                    sqSelected = ()  # reset user clicks
                                    playerClicks = []
                            if not moveMade:
                                playerClicks = [sqSelected]

                # Key handlers
                elif e.type == self.p.KEYDOWN:
                    if e.key == self.p.K_z:  # when user presses 'z' key -- undo the move
                        gs.undoMove()
                        moveMade = True
                        animate = False
                    if e.key == self.p.K_r:  # when user presses 'r' key -- resets the board
                        gs = chessEngine.GameState()
                        validMoves = gs.getValidMoves()
                        sqSelected = ()
                        playerClicks = []
                        moveMade = False
                        animate = False

                # handle moveMade
                if moveMade:
                    if animate:
                        self.animateMove(gs.moveLog[-1], self.screen, self.clock, gs)
                    validMoves = gs.getValidMoves()
                    moveMade = False
                    animate = False

                # Every frame
                self.drawGameState(self.screen, validMoves, sqSelected, gs)

                if gs.checkMate:
                    GameOver = True
                    if gs.whiteToMove:
                        self.drawText(self.screen, 'Black wins by checkmate.')
                    else:
                        self.drawText(self.screen, 'White wins by checkmate.')
                elif gs.staleMate:
                    GameOver = True
                    self.drawText(self.screen, 'Stalemate.')

                self.clock.tick(self.MAX_FPS)
                self.p.display.update()

    # responsible for all the graphics in the current game state
    def drawGameState(self, screen, validMoves, sqSelected, gs):
        self.drawBoard()  # draw squares on the board
        self.highlightSquares(screen, validMoves, sqSelected, gs)
        self.drawPieces(gs)  # draw pieces on top of the board

    def drawBoard(self):
        global colors
        WHITE = (204, 183, 174)
        BLACK = (112, 102, 119)
        colors = [self.p.Color(WHITE), self.p.Color(BLACK)]
        for i in range(self.DIMENSION):
            for j in range(self.DIMENSION):
                color = colors[(i+j) % 2]
                self.p.draw.rect(self.screen, color, self.p.Rect(i*self.SQ_SIZE, j*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def drawPieces(self, gs):
        board = gs.board
        for i in range(self.DIMENSION):
            for j in range(self.DIMENSION):
                piece = board[j][i]
                if piece != "--":
                    self.screen.blit(self.IMAGES[piece], self.p.Rect(i*self.SQ_SIZE, j*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))

    def highlightSquares(self, screen, validMoves, sqSelected, gs):
        if sqSelected != ():
            r, c = sqSelected
            if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b'):
                s = self.p.Surface((self.SQ_SIZE, self.SQ_SIZE))
                s.set_alpha(100)  # 0 -> full transparent, 255 -> full opaque
                s.fill(self.p.Color('blue'))
                screen.blit(s, (c*self.SQ_SIZE, r*self.SQ_SIZE))
                # highlight moves from that square
                s.fill(self.p.Color('yellow'))
                for move in validMoves:
                    if move.startRow == r and move.startCol == c:
                        screen.blit(s, (self.SQ_SIZE*move.endCol, self.SQ_SIZE*move.endRow))

    def animateMove(self, move, screen, clock, gs):
        global colors
        dR = move.endRow - move.startRow
        dC = move.endCol - move.startCol
        framesPerSquare = 10  # frames to move one square
        frameCount = (abs(dR) + abs(dC)) * framesPerSquare
        for frame in range(frameCount + 1):
            r, c = (move.startRow + dR * (frame / frameCount), move.startCol + dC * (frame / frameCount))
            self.drawBoard()
            self.drawPieces(gs)
            # erase the piece moves from the ending square
            color = colors[(move.endRow + move.endCol) % 2]
            endSquare = self.p.Rect(move.endCol*self.SQ_SIZE, move.endRow*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE)
            self.p.draw.rect(screen, color, endSquare)
            # draw captured piece onto Rectangle
            if move.pieceCaptured != "--":
                screen.blit(self.IMAGES[move.pieceCaptured], endSquare)
            # draw the moving piece
            screen.blit(self.IMAGES[move.pieceMoved], self.p.Rect(c*self.SQ_SIZE, r*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
            self.p.display.flip()
            clock.tick(60)

    def drawText(self, screen, text):
        HEIGHT = self.SQ_SIZE*self.DIMENSION
        WIDTH = self.SQ_SIZE * self.DIMENSION
        font = self.p.font.SysFont("Helvetica", 32, True, False)
        textObject = font.render(text, 0, self.p.Color('Gray'))
        textLocation = self.p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2 - textObject.get_width()/2, HEIGHT/2 - textObject.get_height()/2)
        screen.blit(textObject, textLocation)
        textObject = font.render(text, 0, self.p.Color('Black'))
        screen.blit(textObject, textLocation.move(2, 2))