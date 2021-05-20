#include <iostream>
#include <cmath>

using namespace std;

bool check(long n);

int main() {
	int i = 143;
	long n = 0;

	while (true){
		i++;
		n = i * (2 * i - 1);
		if (check(n)){
			cout << n << endl;
			break;
		}
	}
}

bool check(long n){
	double test = (sqrt(1 + 24 * n) + 1.0) / 6.0;
	return test == (int)test;
}
