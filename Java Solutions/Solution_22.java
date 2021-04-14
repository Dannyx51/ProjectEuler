import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.math.*;

/*
 * Problem:
 * Using names.txt [attached], a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
 * For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
 * What is the total of all the name scores in the file?
 * 
 * Solution: 871198282.
 * Average Time: 204.4ms
 * 
 * Alphabetize the list, then find the value of each word and multiply by its position.
 * 
 */

class Main {
	public static void main(String[] args) {
		long start = System.currentTimeMillis();
		double ans = 0;
		
		
		//System.out.println(getAlphaVal('g') > getAlphaVal('b'));
		String[] names = new String[5];
		try {
			File myObj = new File("names.txt");
			Scanner myReader = new Scanner(myObj);
			
			while (myReader.hasNextLine()) {
				String data = myReader.nextLine();
				names = data.split("\",\"");
				names[0] = names[0].substring(1);
				names[names.length-1] = names[names.length-1].substring(0, names[names.length-1].length()-1);
				//System.out.println(names[0]);
				//System.out.println(names[names.length-1]);
			}
			myReader.close();
		} catch (FileNotFoundException e) {
			System.out.println("An error occurred.");
			e.printStackTrace();
		}
		
		names = alpha(names);
		for (int i = 0; i < names.length; i++) ans += (i + 1) * alphaVal(names[i]);
		//System.out.println(names[names.length-1] + " " + (1 * alphaVal(names[names.length - 1])));
		
		long end = System.currentTimeMillis() - start;
		System.out.printf("%f\n", ans);
		System.out.println(end);
	}

	public static String[] alpha(String[] text) {
		ArrayList<String> res = new ArrayList<String>();
		
		for (int i = 0; i < text.length; i++) {
			int pos = -1;
			for (int ii = 0; ii < res.size(); ii++) {
				boolean encontrado = false;
				for (int iii = 0; iii < res.get(ii).length() ; iii++) {
					if (iii >= text[i].length()) {
						encontrado = true;
						break;
					}
					int a = alphaVal(res.get(ii).charAt(iii));
					int b = alphaVal(text[i].charAt(iii));
					if (a > b) {
						encontrado = true;
						//System.out.println(text[i] + " " + res.get(ii));
						break;
					} else if (b > a) break;
				}
				if (encontrado == true) {
					pos = ii;
					break;
				}
			}
			if (pos == -1) res.add(text[i]);
			else res.add(pos, text[i]);
			//printArrayList(res);
		}
		
		String[] ret = new String[res.size()];
		for (int i = 0; i < ret.length; i++) ret[i] = res.get(i);
		
		return ret;
	}

	public static int alphaVal(String text) {
		int sum = 0;
		for (int i = 0; i < text.length(); i++) sum += Integer.valueOf(text.charAt(i)) - 64;
		return sum;
	}
	
	public static int alphaVal(char character) {
		return Integer.valueOf(character) - 64;
	}
	
	public static void printArrayList(ArrayList<String> text) {
		System.out.println('\n');
		for (int i = 0; i < text.size(); i++) System.out.println(text.get(i));
	}
	
}
