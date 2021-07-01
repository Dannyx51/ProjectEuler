import java.math.BigInteger;
import java.util.*;
/*
 * I don't know how to explain this but it works
 * 
 * Uses IntegerAsString.java which is not yet updated on github
 * 
 * ~500 ms
 */

class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;
		
		int[] divisors = {2, 3, 5, 7, 11, 13, 17};
		
		ArrayList<IntegerAsString>[] lists = new ArrayList[7];
		
		for (int i = 0; i < 7; i++)
			lists[i] = new ArrayList<IntegerAsString>();
		
		for (int i = 1000; i < 10000; i++, i++)
			lists[0].add(IntegerAsString.valueOf(i));
		
		for (int i = 0; i < 6; i++) {
			for (int ii = 0; ii < lists[i].size(); ii++)
				for (int iii = 0; iii < 10; iii++) {
					IntegerAsString cur = lists[i].get(ii).append(iii);
					if (cur.subIAS(-3).intValue() % divisors[i + 1] == 0) //checks last three digits of aggregated number to see if they are divisible correctly
						lists[i + 1].add(cur);
				}
		}
		
		for (int i = 0; i < lists[6].size(); i++)
				if (lists[6].get(i).isPandigital(0, 9))
					ans += lists[6].get(i).doubleValue();
			
		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans);
		System.out.println(end);
	}

}
