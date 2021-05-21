#include <iostream>
#include "pHelper.h"
#include <chrono>

using namespace std;
using namespace chrono;

int main() {
	auto start = high_resolution_clock::now();
	int n = 3;
 	while (true){
		bool flag = false;
		if (!isPrime(n)){
			for (int i = 2; i < n - 1; i++){
				if (isPrime(i)){
					//cout << n << ": " << i << endl;
					int diff = n - i;
					//cout << diff << endl;
					int res = 0;
					int inc = 1;
					while (res <= diff){
						res = 2 * pow(inc, 2);
						if (res + i == n){
							//cout << n << ": " << i << " + (2 * (" << inc << " ^ 2))" << endl;
							flag = true;
						}
						inc++;
						if (flag){
							break;
						}
					}
				}
				if (flag){
					break;
				}
			}
			if (!flag){
				auto end = high_resolution_clock::now();
				auto dura = duration_cast<milliseconds>(end - start);
				cout << n << endl;
				cout << "Solution found in " << dura.count() << " milliseconds" << endl;
				break;
			}
		}
		n += 2;
  	}
}
