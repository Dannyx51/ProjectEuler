import java.util.*;

/*
 * Problem:
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 * 
 * Solution: 233168
 * Average Time: 0ms
 * 
 * Loops through 1-1000 and adds to a sum if the # is divisible by 3 or 5
 */

class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		int ans = 0;

		for (int i = 0; i < 1000; i++)
			ans += i % 3 == 0 || i % 5 == 0 ? i : 0;

		long end = System.currentTimeMillis() - start;
		System.out.println(ans);
		System.out.println(end);
	}
}
