import java.util.*;

/*
 * Solution: 233168
 * Average Time: 0ms
 * 
 * Loops through 1-1000 and adds to a sum if the # is divisible by 3 or 5
 */

class Main {
	  public static void main(String[] args) {
		  long start = System.currentTimeMillis();
			int ans = 0;
			
			for (int i = 0; i < 1000; i++) ans += i % 3 == 0 || i % 5 == 0 ? i : 0;
			
		    long end = System.currentTimeMillis() - start;
		    System.out.println(ans);
		    System.out.println(end);
		    
	  }
}
