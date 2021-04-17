/*
 * Problem:
 * In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
 * 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
 * It is possible to make £2 in the following way:
 * 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
 * How many different ways can £2 be made using any number of coins?
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
 */

class Main {

	static int[] vals = { 1, 2, 5, 10, 20, 50, 100, 200 };

	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;

		int total = 200;
		ans = calcPoss(total, 0, total + 1);

		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans);
		System.out.println(end);
	}

	public static int calcPoss(int total, int val, int least) {
		int res = 0;
		if (total == val)
			res++;
		if (val > total)
			return res;
		for (int i = 0; i < vals.length; i++)
			if (vals[i] <= least)
				res += calcPoss(total, val + vals[i], vals[i] < least ? vals[i] : least);
		return res;
	}
}
