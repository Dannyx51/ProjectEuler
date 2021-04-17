/*
 * Problem:
 * Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
 * 1634 = 1^4 + 6^4 + 3^4 + 4^4
 * 8208 = 8^4 + 2^4 + 0^4 + 8^4
 * 9474 = 9^4 + 4^4 + 7^4 + 4^4
 * As 1 = 14 is not a sum it is not included.
 * The sum of these numbers is 1634 + 8208 + 9474 = 19316.
 * Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
 * 
 * Solution: 443839
 * Average Time: 351.2ms
 *
 * Literally check each number from a lower limit to an upper limit to see if it fits the function.
 * Determining the upper limit was difficult, but because the highest 7 digit number is 9999999, and the
 * function's output for this number is less than a 7 digit number, it is impossible for an eight digit number
 * to work for the function. So the upper limit is 9^5 * 7.
 * 
 * Uses IntegerAsString.java
 * 
 */

class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;

		IntegerAsString upperLimit = new IntegerAsString(IntegerAsString.multiply(IntegerAsString.pow(9, 5), "7"));
		
		for (IntegerAsString i = new IntegerAsString("2"); i.isLessThan(upperLimit); i.increment())
			if (i.equals(IntegerAsString.valueOf(sumPower(i.digits(), 5))))
				ans += i.intValue();

		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans);
		System.out.println(end);
	}

	public static int sumPower(int[] digits, int power) {
		int res = 0;
		for (int i = 0; i < digits.length; i++)
			res += Math.pow(digits[i], power);
		return res;
	}
}
