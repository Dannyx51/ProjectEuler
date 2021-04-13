import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.math.*;

/*
 * Problem:
 * Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
 * If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
 * For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
 * Evaluate the sum of all the amicable numbers under 10000.
 * 
 * Solution: 31626
 * Average Time: 304.2ms
 * 
 * Looping up to 10000, if i is equal to the sum of the divisors of the sum of the divisors of i, then
 * add i to total
 * 
 */

class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;
		
		for (int i = 1; i < 10000; i++) if (i != d(i) && i == d(d(i))) ans += i;

		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans);
		System.out.println(end);
	}

	public static int d(int x) {
		int sum = 0;
		
		for (int i = 1; i < x; i++) {
			if (x % i == 0) sum += i;
		}
		
		return sum;
	}

}
