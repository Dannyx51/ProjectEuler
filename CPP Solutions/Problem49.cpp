#include <iostream>
#include <chrono>
#include "pHelper.h"
#include <algorithm>

using namespace std;
using namespace chrono;

bool isPermu(string a, string b);

int main() {
	auto start = high_resolution_clock::now();
	string ans = "";
	for (int i = 1001; i < 10000 - 3330; i += 2){
		if (isPrime(i)){
			int n1 = i;
			int n2 = n1 + 3330;
			int n3 = n2 + 3330;
			if (isPermu(to_string(n1), to_string(n2))){
				if (isPermu(to_string(n2), (to_string(n3)))){
					if (isPrime(n2) && isPrime(n3)){
						ans = to_string(n1) + to_string(n2) + to_string(n3);
					}
				}
			}
		}
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<milliseconds>(end - start);
	cout << ans << endl;
	cout << "Solution found in " << dura.count() << " milliseconds" << endl;
}

bool isPermu(string a, string b){
	sort(a.begin(), a.end());
	sort(b.begin(), b.end());
	if (a == b){
		return true;
	}
	return false;
}
