#! /usr/bin/env python3
import copy

class GameOfLife():
    def run(self, board_input):
        # Sample: "-3,-5 -4,-5"
        # Board is dict(x, list of ys)
        # Builds board from input
        board = {}
        for raw_cord in board_input.split(' '):
            raw_x, raw_y = raw_cord.split(',')
            x, y = int(raw_x), int(raw_y)
            if x not in board:
                board[x] = []
            board[x].append(y)

        # Apply rules to board
        next_board = copy.deepcopy(board)
        for x in board.keys():
            for y in board[x]:
                num_live_neighbors = self.countNumLiveNeighbors(board, x, y)
                if num_live_neighbors < 2 or num_live_neighbors > 3:
                    # Remove (x,y) from next_board
                    next_board[x].remove(y)
                    if not next_board[x]:
                        next_board.pop(x)

        # Print next_board
        output_pairs = []
        for x in next_board.keys():
            for y in next_board[x]:
                output_pairs.append((x, y))
        output_pairs = sorted(output_pairs)
        print(" ".join(output_strs))


    def countNumLiveNeighbors(self, board, x, y):
        # Count up the number of live neighbors for given (x,y)
        count = 0

        for x_offset in [-1,0,1]:
            for y_offset in [-1,0,1]:
                if x_offset == 0 and y_offset == 0:
                    continue
                new_x = x + x_offset
                new_y = y + y_offset
                if new_x in board and new_y in board[new_x]:
                    count += 1
        return count

if __name__ == "__main__":
    GameOfLife().run()
