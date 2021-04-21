#include <iostream>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace chrono;

bool areSame(int n1, int n2, int N1, int N2);

int main() {
	auto start = high_resolution_clock::now();
	int num = 1;
	int den = 1;
	for (int n1 = 10; n1 < 100; n1++){
		for (int n2 = 10; n2 < 100; n2++){
			int r1 = stoi(to_string(n1).substr(1, 1));
			int r2 = stoi(to_string(n2).substr(0, 1));
			if (r1 == r2 && n1 % 11 != 0){
				int N1 = stoi(to_string(n1).substr(0, 1));
				int N2 = stoi(to_string(n2).substr(1, 1));
				if (areSame(n1, n2, N1, N2)){
					num *= n1;
					den *= n2;
				}
			}
		}
	}
	int d;
	d = __gcd(num, den);
	den = den / d;
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<milliseconds>(end - start);
	cout << den << endl;
	cout << "Solution found in " << dura.count() << " milliseconds" << endl;
}

bool areSame(int n1, int n2, int N1, int N2){
	if (double(n1) / double(n2) == double(N1) / double(N2)){
		return true;
	}
	return false;
}

// Best runtime is 12 milliesconds poggers
