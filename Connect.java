public class Connect {
	static int[][] board = {
			{0, 0, 0, 0, 0, 0, 0},
			{0, 0, 0, 0, 0, 0, 0},
			{0, 0, 0, 0, 0, 0, 0},
			{0, 0, 0, 0, 0, 0, 0},
			{0, 0, 0, 0, 0, 0, 0},
			{1, 1, 1, 1, 0, 0, 0},
	};

	/**
	 * Integer representing a blank space
	 */
	public static final int BLANK = 0;
	/**
	 * Integer representing a yellow checker
	 */
	public static final int YELLOW = 1;
	/**
	 * Integer representing a red checker
	 */
	public static final int RED = 2;

	/**
	 * Main function, checks every space for a win
	 * @return Team that won
	 */
	public static int process() {
		for (int y = 0; y < 6; y++) {
			for (int x = 0; x < 7; x++) {
				for (int direction = 0; direction < 4; direction ++) {
					if (board[y][x] != BLANK && check(0, board[y][x], x, y, direction)) {
						return board[y][x] == YELLOW ? YELLOW : RED;
					}
				}
			}
		}
		return BLANK;
	}

	/**
	 * Recursive solution that checks to see if 4 checkers extend out from the given
	 * checker, in the given direction. It checks to ensure that the four do not try
	 * to exceed past the edge of the board, and that the checkers are always the same
	 * color. If the recursion reaches the depth of four, it finishes.
	 * @param n amount of checkers in a row so far
	 * @param team team of the checkers in a row so far
	 * @param x x of current checker
	 * @param y y of current checker
	 * @param direction direction for search. 0 is horizontal right,
	 *  1 is diagonal down left, 2 is vertical, 3 is diagonal down right
	 * @return whether there are four checkers in a row, based on the parameters
	 */
	public static boolean check(int n, int team, int x, int y, int direction) {
        if (board[y][x] == team) {
            if (n == 3)
                return true;
            switch (direction) {
            case 0:
                if (x != 6)
                	return check(n+1, team, x + 1, y, direction);
            case 1:
                if (x != 6 && y != 5)
                	return check(n + 1, team, x + 1, y + 1, direction);
            case 2:
                if (y != 5)
                	return check(n + 1, team, x, y + 1, direction);
            default:
                if (x != 0 && y != 5)
                	return check(n + 1, team, x - 1, y + 1, direction);
            }
        }
        return false;
	}
}
