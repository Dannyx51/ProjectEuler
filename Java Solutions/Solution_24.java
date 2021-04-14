import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.math.*;

/*
 * Problem:
 * A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
 * 012   021   102   120   201   210
 * What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
 * 
 * Solution: 278391560.
 * Average Time: 0.6ms
 * 
 * There are 10! permutations. If we assume the first digit is 0, there will be 9! permutations of
 * the other 9 digits. Since 9! < 1000000, we know the first digit is actually higher 
 * than 0 because the first 9! permutations begin with the digit 0. 
 * In fact, the first digit is higher than 1. However,
 * since 9! * 4 > 1000000 (9! * 4 would cover all permutations beginning with 0, 1, 2, & 3),
 * we know the first digit is lower than 3.
 * Using this process of elimination method all the way through, each digit of the answer reveals itself.
 * 
 */

class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;		
		

		ArrayList<Integer> nums = new ArrayList<Integer>();
		for (int i = 0; i < 10; i++) nums.add(i);
		
		String result = "";
		long yet = 1000000;
		for (int i = 9; i > 0; i--) {
			long poss = factorial(i);
			int digit = (int) (yet / poss);
			result += nums.remove(digit);
			yet -= (digit * poss);
		}
		
		ans = Long.valueOf(result);
		
		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans); 
		System.out.println(end);
	}
	
	public static long factorial(long n) {
		return n == 1 ? n : n * factorial(n - 1);
	}
}
