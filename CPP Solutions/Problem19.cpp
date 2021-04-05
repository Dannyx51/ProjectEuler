#include <iostream>

using namespace :: std;

// Zellers congruence
//F=k+ [(13*m-1)/5] +D+ [D/4] +[C/4]-2*C where
//k is  the day of the month.
//m is the month number.
//D is the last two digits of the year.
//C is the first two digits of the year.

bool found(int k, int m, int d, int c){
	if ((k + ((13 * m - 1) / 5) + d + (d / 4) + (c / 4) - 2 * c) % 7 == 0){
		return true;
	}
	return false;
}

int main() {
	int num = 0;
	for (int year = 1901; year <= 2000; year++){
		int d = stoi(to_string(year).substr(2,2));
		int c = stoi(to_string(year).substr(0,2));
		for (int month = 1; month <= 12; month++){
			if (found(1, month, d, c)){
				num++;
			}
		}
	}
	cout << num << endl;
}
