@author Lincoln Edsall 

public class IntegerAsString {
	
	private String num;
	
	public IntegerAsString() {
		this.num = "0";
	}
	public IntegerAsString(String num) {
		this.num = num;
	}
	
	public int length() {
		return num.length();
	}
	
	public static IntegerAsString valueOf(int x) {
		return new IntegerAsString(String.valueOf(x));
	}
	public String toString() {
		return this.num;
	}
	
	public boolean equals(IntegerAsString x) {
		return this.num.equals(x.toString());
	}
	
	public IntegerAsString add(IntegerAsString x) {
		return new IntegerAsString(add(this.num, x.toString()));
	}
	
	public IntegerAsString multiply(IntegerAsString x) {
		return new IntegerAsString(multiply(this.num, x.toString()));
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
	
	public static String pow(int a, int b) {
		String num = String.valueOf(a);
		String ans = multiply(num, num);
		for (int i = 2; i < b; i++) ans = multiply(ans, num);
		return ans;
	}
	
}
