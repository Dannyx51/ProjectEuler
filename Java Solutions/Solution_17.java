import java.util.*;
import java.math.*;

/*
 * Problem:
 * If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 * If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
 * NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
 * 
 * Solution: 21124
 * Average Time: 2.6ms
 * 
 * Loops through each number and creates a string without spaces and hyphens to represent the number.
 * Adds string length to the total.
 * 
 */


class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;
		
		String[] nums = 
			{"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
			"eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
			"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
			"hundred", "thousand", "and"};
		
		for (int i = 0; i <= 1000; i++) {
			String temp = "";
			if (i < 20) {
				temp = nums[i];
			} else if (i < 100) {
				temp = nums[18 + getDigit(i, 1)] +  nums[getDigit(i, 0)];
			} else if (i < 1000) {
				if (i % 100 == 0) {
					temp = nums[getDigit(i, 2)] + nums[28];
				} else if (getDigit(i, 1) == 1) {
					temp = nums[getDigit(i, 2)] + nums[28] + nums[30] + nums[10 + getDigit(i, 0)];
				} else if (getDigit(i, 1) == 0) {
					temp = nums[getDigit(i, 2)] + nums[28] + nums[30] + nums[getDigit(i, 0)];
				} else {
					temp = nums[getDigit(i, 2)] + nums[28] + nums[30] + nums[18 + getDigit(i, 1)] +  nums[getDigit(i, 0)];
				}
			} else if (i == 1000) temp = nums[1] + nums[29];
			ans += temp.length();
			//System.out.println(i + " " + temp + " " + temp.length());
		}
	
		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans);
		System.out.println(end);
	}
	
	public static int getDigit(int n, int x) {
		int ans = n;
		if (x == 0) ans = ans % 10;
		if (x == 1) ans = getDigit((ans - getDigit(ans, 0)) / 10, 0);
		if (x == 2) {
			while (ans > 9) {
				ans = (ans - (ans % 10)) / 10;
			}
		}
		
		return ans;
	}
	

}
