/*
 * Problem:
 * We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
 * The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
 * Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
 * HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
 * 
 * Solution: 73682
 * Average Time: 35.2ms
 *
 * Recursion time :)
 * The recursion function starts with the biggest denominations and works its way to the smaller ones:
 * To be sure there are no duplicates, once a denomination is used in a combo, 
 * a higher one cannot be used again in the combo. Also the function uses integers instead
 * of decimals because easier.
 * 100 + 50 + 20 + 10 + 10 + 10 == 200 is one of the combos, but
 * 50 + 100 + 10 + 10 + 10 + 20 == 200 will never be one of them.
 * 
 * Uses IntegerAsString.java
 * 
 */

class Main {

	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;

		System.out.println(isPan(1333, 1, 1333));
		
		for (int i = 1000; i < 10000; i++)
			for (int ii = 1; ii < 100; ii++)
				if (i % ii == 0)
					if (isPan(i, ii, i / ii)) {
						ans += i;
						break;
					}

		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans);
		System.out.println(end);
	}

	public static boolean isPan(int a, int b, int c) {
		IntegerAsString combo = new IntegerAsString(String.valueOf(a) + String.valueOf(b) + String.valueOf(c));
		int[] digits = combo.digits();
		boolean[] check = new boolean[10];
		for (int i = 0; i < digits.length; i++) 
			check[digits[i]] = true;
		for (int i = 1; i < check.length; i++) 
			if (check[i] != true) return false;
		return true;
	}
}
