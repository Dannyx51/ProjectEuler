#include <iostream>
#include <cmath>
#include <chrono>

using namespace std;
using namespace chrono;

int pent(int n);
bool isPent(int n);

int main() {
	auto start = high_resolution_clock::now();
	int i = 0;
	while (true){
		i++;
		int j = pent(i);
		for (int ii = i - 1; ii > 0; ii--){
			int k = pent(ii);
			if (isPent(abs(j - k)) && isPent(j + k)){
				auto end = high_resolution_clock::now();
				auto dura = duration_cast<milliseconds>(end - start);
				cout << abs(j - k) << endl;
				cout << "Solution found in " << dura.count() << " milliseconds" << endl;
				return 0;
			}
		}
	}
}

int pent(int n){
	return (n * ((3 * n) - 1)) / 2;
}

bool isPent(int n){
	double t = (sqrt(1 + (24 * n)) + 1) / 6;
	return t == int(t);
}
