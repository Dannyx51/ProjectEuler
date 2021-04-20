/*
 * Problem:
 * 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
 * Find the sum of all numbers which are equal to the sum of the factorial of their digits.
 * Note: As 1! = 1 and 2! = 2 are not sums they are not included.
 * 
 * Solution: 40730
 * Average Time: 1871.4ms
 *
 * Works very similarly to #30. Find the upper limit then loop checking if the numbers in the range
 * fit the function;
 * 
 * Uses IntegerAsString.java
 * 
 */

class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;
		
		IntegerAsString upperLimit = new IntegerAsString("0");
		for (int i = 0; true; i++) {
			String nineFactMultiple = IntegerAsString.multiply(IntegerAsString.factorial(9), String.valueOf(i));
			if (nineFactMultiple.length() < i) {
				upperLimit = new IntegerAsString(nineFactMultiple);
				break;
			}
		}
		
		for (IntegerAsString i = new IntegerAsString("3"); i.isLessThan(upperLimit); i.increment())
			if (i.equals(IntegerAsString.valueOf(sumFact(i.digits()))))
				ans += i.intValue();

		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans);
		System.out.println(end);
	}

	public static int sumFact(int[] digits) {
		int res = 0;
		for (int i = 0; i < digits.length; i++) {
			res += factorial(digits[i]);
		}
		return res;
	}
	
	public static int factorial(int n) {
		return n == 1 || n == 0 ? 1 : n * factorial(n - 1);
	}
}
