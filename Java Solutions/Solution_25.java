import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.math.*;

/*
 * Problem:
 * The Fibonacci sequence is defined by the recurrence relation:
 * Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
 * Hence the first 12 terms will be:
 * F1 = 1 F2 = 1 F3 = 2 F4 = 3 F5 = 5 F6 = 8 F7 = 13 F8 = 21 F9 = 34 F10 = 55 F11 = 89 F12 = 144
 * The 12th term, F12, is the first term to contain three digits.
 * What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
 * 
 * Solution: 2783915460.
 * Average Time: 0.6ms
 *
 * Just do the sequence.
 * 
 */

class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;		
		
		int c = 2;
		String res = "1";
		String back = "1";
		
		while  (ans < 1000) {
			String temp = add(res, back);
			back = res;
			res = temp;
			ans = res.length();
			c++;
		}
		ans = c;
			
		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans); 
		System.out.println(end);
	}
	
	public static String add(String num1, String num2) {
		String ans = "";
		
		int num1l = num1.length();
		int num2l = num2.length();
		
		String a = num1l >= num2l ? num1 : num2;
		String b = num1l >= num2l ? num2 : num1;
		int al = a.length();
		int bl = b.length();
		
		int overflow = 0;
		for (int i = 0; i < al; i++) {
			int posa = al - i - 1;
			int posb = bl - i - 1;
			
			int col = Integer.valueOf(a.substring(posa, posa + 1)) + (posb >= 0 ? Integer.valueOf(b.substring(posb, posb + 1)) : 0);

			col += overflow;
			overflow = (col - (col % 10)) / 10;
			col = col % 10;
			
			ans = (i == al - 1 ? String.valueOf(overflow) : "") + col + ans;
		}
		
		while (true) {
			if (ans.length() == 0) {
				ans = "0";
				break;
			}
			if (!ans.substring(0, 1).equals("0")) break;
			ans = ans.substring(1);
		}
		
		return ans;
	}
}
