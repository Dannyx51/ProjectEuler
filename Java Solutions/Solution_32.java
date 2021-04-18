/*
 * Problem:
 * We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
 * The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
 * Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
 * HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
 * 
 * Solution: 45228
 * Average Time: 66.4ms
 *
 * It appears to me that in any given x * y = z, where len(n) equals the number of digits in the number n:
 * len(x) + len(y) = len(x) 
 * OR 
 * len(x) + len(y) = len(x) + 1
 * I don't know how true this is, but it turned out alright for this problem. Assuming it is true,
 * and knowing that the numbers in the multiplicand/multiplier/product identity have to have a total length of 9,
 * len(1) * len(4) = len(4) and len(2) * len(3) = len(4) are the only possibilities for pandigital identities.
 * So, looping through every 4 digit number and checking if it can be divided by a 1 or 2 digit number
 * gives possible pandigital identities.
 * The pandigital method checks to see if the digits of the identity contain each number 1-9 by
 * splitting up the identity into an integer array and comparing with a boolean array.
 * 
 * Uses IntegerAsString.java
 * 
 */

class Main {

	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;
		
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
