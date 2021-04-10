import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.math.*;

/*
 * You are given the following information, but you may prefer to do some research for yourself.
 * 1 Jan 1900 was a Monday.
 * Thirty days has September,
 * April, June and November.
 * All the rest have thirty-one,
 * Saving February alone,
 * Which has twenty-eight, rain or shine.
 * And on leap years, twenty-nine.
 * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
 * How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
 * 
 * Solution: 171
 * Average Time: 0ms
 * 
 * Looping through each year, and within that looping through each month, we can check numDays' divisibility.
 * numDays % 7 = n, where n corresponds to the day of the week on which the month started (0 == monday, 6 == sunday)
 * After this check, the number of days in the month must be added to numDays.
 * 
 */

class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;

		int[] months = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

		// String[] monthNames = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
		// "Aug", "Sep", "Oct", "Nov", "Dec"};
		// String[] dayNames = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}

		int numDays = 0; // Jan 1, 1900 was a Monday == 0

		for (int i = 1900; i < 2001; i++)
			for (int ii = 0; ii < months.length; ii++) {
				if (i != 1900)
					if (numDays % 7 == 6)
						ans++;
				numDays += months[ii] + (isLeap(i) && ii == 1 ? 1 : 0); // accounts for leap year

				// if (numDays % 7 == 6) System.out.println(dayNames[numDays % 7] + " " +
				// monthNames[ii] + ", " + i);
			}

		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans);
		System.out.println(end);
	}

	public static boolean isLeap(int year) {
		return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
	}

}
