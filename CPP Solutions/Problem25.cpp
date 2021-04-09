#include <iostream>
#include <vector>
#include <string>
#include <vector>
#include <chrono>

using namespace std;
using namespace chrono;

string addString(string a, string b){
/*
    1.
        a. First I'll split the string into a list
            of ints to make it easier to work with
        b. I'll make two string lengths equal to each   other

    2.  Then I'll go down the columns, from right to
        left, and add in order.
    
    3.
        a. If the resulting int has one digit
            continue to the next iteration
        b. if the resulting int has more than one
            digit, we will split the number into two 
            parts
        c. The first part is the remainder
            (everything except the last digit)
        d.  if the resulting int has more than one
            digit, we will split the number into two parts

    4. The remainder gets added to the next column in
        the second row (just incase num2 is longer than num1)
    
    5. We will keep a running vector of digits until
        we are left with just the remainder
    
    6. We can then add the remainder to the first
        position in the string and return as such
*/

	// Step 1a
	int as = a.length();
	int bs = b.length();
	int aDigi[bs];
	// Step 1b
	string strO = "";
	if (bs > as){
		int o = bs - as;
		for (int i = 0; i < o; i++){
			strO += "0";
		}
	}
	a = strO + a;
	for (int i = 0; i < a.length(); i++){
		aDigi[i] = stoi(a.substr(i, 1));
	}
	int bDigi[bs];
	for (int i = 0; i < b.length(); i++){
		bDigi[i] = stoi(b.substr(i, 1));
	}
	// Step 2
	int r = 0;
	vector<int> vDigi;
	for (int i = (sizeof(aDigi) / sizeof(int)) - 1; i >= 0; i--){
		// Step 4
		int sum = aDigi[i] + bDigi[i] + r;
		r = 0;
		// Step 3
		if (to_string(sum).length() > 1){
			int s = to_string(sum).length();
			int d = stoi(to_string(sum).substr(s - 1, 1));
			r = stoi(to_string(sum).substr(0, s - 1));
			// Step 5
			vDigi.insert(vDigi.begin(), d);
			//cout << r << " and " << d << endl;
		} else {
			// Step 5
			vDigi.insert(vDigi.begin(), sum);
			//cout << sum << endl;
		}
	}
	// Step 6
	vDigi.insert(vDigi.begin(), r);
	string c = "";
	for (int i = 0; i < vDigi.size(); i++){
		c += to_string(vDigi.at(i));
	}
	// Test return statement
	return c;
}

//Function for removing zeros infront of all these numbers
string trimZ(string s){
	int n = 0;
	for (int i = 0; n < s.length(); i++){
		if (s.substr(i, 1) != "0"){
			break;
		}
		n++;
	}
	//cout << "^ Number of zeros in number above ^: " << n << endl;
	//cout << "Test for isolating numbers: " << s.substr(n,s.length() - 1) << endl;
	return s.substr(n,s.length());
}

//4294967294
int main() {
	auto start = high_resolution_clock::now();
	vector<string> fib;
	fib.insert(fib.begin() + 0, "1");
	fib.insert(fib.begin() + 1, "1");
	int i1 = 0;
	int i2 = 1;
	int i3 = 2;
	bool found = false;
	//addString(n1, n2);
	while (!found){
		fib.push_back(trimZ(addString(fib.at(i1), fib.at(i2))));
		//cout << fib.at(i3) << endl;
		if (fib.at(i3).length() == 1000){
			auto end = high_resolution_clock::now();
			auto duro = duration_cast<microseconds>(end - start);
			cout << i3 + 1 << endl;
			cout << "Solution found in " << duro.count() << " microseconds" << endl;
			return 0;
		}
		//cout << i3 << endl;
		i1++;
		i2++;
		i3++;
	}
}
