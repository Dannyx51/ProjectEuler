#include <iostream>
#include <cmath>
#include <chrono>

using namespace std;
using namespace chrono;

bool check(long n);

int main() {
	auto start = high_resolution_clock::now();
	int i = 143;
	long n = 0;

	while (true){
		i++;
		n = i * (2 * i - 1);
		if (check(n)){
			auto end = high_resolution_clock::now();
			auro dura = duration_cast<milliseconds>(end - start);
			cout << n << endl;
			cout << "Solution found in " << dura.count() << " milliseconds" << endl;
			break;
		}
	}
}

bool check(long n){
	double test = (sqrt(1 + 24 * n) + 1.0) / 6.0;
	return test == (int)test;
}
