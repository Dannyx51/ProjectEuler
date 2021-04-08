import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.math.*;

/*
 * Problem:
 * By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
 * 3
 * 7 4
 * 2 4 6
 * 8 5 9 3
 * That is, 3 + 7 + 4 + 9 = 23.
 * Find the maximum total from top to bottom of the triangle [in the attached file]
 * NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
 * 
 * Solution: 1074
 * Average Time: 85.2ms
 * 
 * On the second to last row (1), each number (n) only has two possible paths to choose from
 * on the row below it (0).
 * The larger number (L) below a given n on row 1 be the path that n chooses in all cases.
 * Each L in row 0 can be added to each n in row 1, so that row 0 can be "deleted"/ignored.
 * If this is repeated up the triangle, the last number remaining will be the answer.
 * 
 */

class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;


		ArrayList<ArrayList<Integer>> grid = new ArrayList<ArrayList<Integer>>();
		try {
			File myObj = new File("nums.txt");
			Scanner myReader = new Scanner(myObj);
			int c = 0;
			while (myReader.hasNextLine()) {
				String data = myReader.nextLine();
				String[] row = data.split(" ");
				grid.add(new ArrayList<Integer>());
				for (int i = 0; i < row.length; i++) {
					grid.get(c).add(Integer.valueOf(row[i]));
				}
				c++;
			}
			myReader.close();
		} catch (FileNotFoundException e) {
			System.out.println("An error occurred.");
			e.printStackTrace();
		}
		
		for (int i = grid.size() - 2; i >= 0; i--) {
			ArrayList<Integer> cur = grid.get(i);
			ArrayList<Integer> under = grid.get(i + 1);
			for (int ii = 0; ii < grid.get(i).size(); ii++) {
				int num = cur.get(ii);
				int unL = under.get(ii);
				int unR= under.get(ii + 1);
				cur.set(ii, unL > unR ? num + unL : num + unR);
			}
		}
		ans = grid.get(0).get(0);

		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans);
		System.out.println(end);
	}

}