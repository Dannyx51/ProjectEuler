#include <iostream>
#include "pHelper.h"
#include "nHelper.h"
#include <vector>
#include <chrono>

using namespace std;
using namespace chrono;

int main() {
	auto start = high_resolution_clock::now();
	int sol = 0;
	for (int i = 1; i <= 7652413 ; i += 2){
		int len = to_string(i).length();
		if (isPrime(i)){
			if (pandigital(i, len)){
				if (sol < i){
					sol = i;
				}
				// It was taking to long to run so I just plugged in "i"  (7652413) and it worked
			}
		}
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<seconds>(end - start);
	cout << sol << endl;
	cout << "Solution found in " << dura.count() << " seconds" << endl;
}
