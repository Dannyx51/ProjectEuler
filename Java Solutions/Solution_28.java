import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.math.*;

/*
 * Problem:
 * Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
 * 21 22 23 24 25
 * 20  7  8  9 10
 * 19  6  1  2 11
 * 18  5  4  3 12
 * 17 16 15 14 13
 * It can be verified that the sum of the numbers on the diagonals is 101.
 * What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
 * 
 * Solution: 669171001
 * Average Time: 0ms
 *
 * The corner numbers of each inner-square (1x1, 3x3, etc) follow a pattern. The first four are found by
 * adding 2 the previous, the next four are found by adding 4 to the previous. Then 6, then 8, and so on.
 * 
 */

class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;

		int x = 2;
		int c = 0;
		ans++; // accounts for the number 1 at the center
		for (int i = 3; i <= 1001 * 1001; i += x) {
			// System.out.println(i);
			ans += i;
			c++;
			if (c == 4) {
				c = 0;
				x += 2;
			}
		}

		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans);
		System.out.println(end);
	}
}
