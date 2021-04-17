import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.math.*;

/*
 * Problem:
 * A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
 * 1/2=0.5 1/3=0.(3) 1/4=0.25 1/5=0.2 1/6=0.1(6) 1/7=0.(142857) 1/8=0.125 1/9=0.(1) 1/10 = 0.1
 * Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
 * Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
 * 
 * Solution: 983
 * Average Time: 33.2ms
 *
 * In a similar method to long-hand division, one divided by a given number (n)
 * can be determined by doing (int) 10 / n, then (int) 10(10 % n) / n, and looping that.
 */

class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;		
		
		Tuple<Integer, Integer> result = new Tuple<Integer, Integer>(0, 0);
		
		for (int i = 2; i < 1000; i++) {
			int c = 0;
			ArrayList<Long> alma = new ArrayList<Long>();
			alma.add((long) 1);
			for (long ii = 1; true; ii *= 10) {
				if (ii == 0) break;
				if (ii < i) continue;
				if (alma.contains(ii)) break;
				else alma.add(ii);
				ii = ii % i;
				c++;
			}
			if (c > result.y()) result.xy(i, c);
		}
		
		ans = result.x();
			
		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans); 
		System.out.println(end);
	}
}
