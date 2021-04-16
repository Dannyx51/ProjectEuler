import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.math.*;

/*
 * Problem:
 * Euler discovered the remarkable quadratic formula: n^2+n+41.
 * It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
 * However, when n=40, 40^2+40+41 is divisible by 41, and certainly when n=41, 41^2+41+41 is clearly divisible by 41.
 * The incredible formula n^2-79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79.
 * The product of the coefficients, −79 and 1601, is −126479.
 * Considering quadratics of the form: n^2+an+b, where |a|<1000 and |b|≤1000
 * where |n| is the modulus/absolute value of n e.g. |11|==11 and |-4|=4.
 * Find the product of the coefficients, a and b, for the quadratic expression that 
 * produces the maximum number of primes for consecutive values of n, starting with n=0.
 * 
 * Solution: -59231
 * Average Time: 1472.2ms
 *
 * Loop from -1000 to 1000 for a and b, and within the nested for loops test how long n returns a prime value with
 * the value of a and b. (0->)
 * 
 * Uses Tuple.java
 */

class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;

		ArrayList<Integer> primes = genPrimes(2000000);


		Tuple<Integer, Integer> result = new Tuple<Integer, Integer>(0, 0);

		for (int i = -999; i < 1000; i++)
			for (int ii = -1000; ii <= 1000; ii++) {
				int c = 0;
				while (isPrime(quadratic(i, ii, c), primes))
					c++;
				if (c > result.y())
					result.xy(i * ii, c);
			}
			// System.out.println(i);

		ans = result.x();

		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans);
		System.out.println(end);
	}

	public static int quadratic(int a, int b, int n) {
		return (n * n) + (a * n) + b;
	}

	public static boolean isPrime(int x, ArrayList<Integer> primes) {
		for (int i = 0; i <= x; i++)
			if (primes.get(i) == x)
				return true;
		return false;
	}

	public static ArrayList<Integer> genPrimes(int n) {
		boolean[] checks = new boolean[n];
		ArrayList<Integer> primes = new ArrayList<Integer>();
		for (int i = 2; i < checks.length; i++)
			checks[i] = true;
		for (int i = 2; i * i < n + 1; i++)
			if (checks[i] == true)
				for (int ii = i * i; ii < n; ii += i)
					checks[ii] = false;
		for (int i = 0; i < checks.length; i++)
			if (checks[i] == true)
				primes.add(i);
		return primes;
	}
}
