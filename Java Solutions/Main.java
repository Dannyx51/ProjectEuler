import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.math.*;

/*
 * Problem:
 * n! means n × (n − 1) × ... × 3 × 2 × 1
 * For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
 * and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
 * Find the sum of the digits in the number 100!
 * 
 * Solution: 648
 * Average Time: 25.4ms
 * 
 * As 100! is too large for any primitive type to hold, I decided to represent the numbers
 * involved in this problem as strings (int[] array would have been another route).
 * The multiplication function works by taking advantage of long-hand multiplication
 * and the addition function, which works by taking advantage of long-hand addition. Then a loop
 * adds the digits.
 * 
 */

class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;
		
		String res = "1";
		
		System.out.println(multiply("100", "10"));
		
		for (int num = 100; num > 0; num--) {
			res = multiply(res, String.valueOf(num));
		}
		
		for (int i = 0; i < res.length(); i++) ans += Integer.valueOf(res.substring(i, i + 1));


		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans);
		System.out.println(end);
	}
	
	public static String multiply(String num1, String num2) {
		String ans = "0";
		
		int num1l = num1.length();
		int num2l = num2.length();
		
		String a = num1l >= num2l ? num1 : num2;
		String b = num1l >= num2l ? num2 : num1;
		int al = a.length();
		int bl = b.length();
		
		String[] ress = new String[al];
		
		int bega = al - 1;
		int begb = bl - 1;
		
		for (int i = begb; i >= 0; i--) {
			String cur = new String();
			int overflow = 0;
			
			for (int ii = bega; ii >= 0; ii--) {
				
				int posa = Integer.valueOf(a.substring(ii, ii + 1));
				int posb = Integer.valueOf(b.substring(i, i + 1));
				
				int col = posa * posb;
				col += overflow;
				overflow = (col - (col % 10)) / 10;
				col = col % 10;

				cur = (ii == 0 ? String.valueOf(overflow) : "") + col + cur;
				
			}
			for (int ii = 0; ii < begb - i; ii++) cur += "0";
			ress[i] = cur;
		}
		

		for (int i = 0; i < ress.length; i++) {
			if (ress[i] == null) continue;
			ans = add(ans, ress[i]);
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
