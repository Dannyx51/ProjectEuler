#include <iostream>
#include "pHelper.h"
#include <vector>
#include <algorithm>
#include <chrono>

using namespace std;
using namespace chrono;

vector<int> pFactorization(int n);

int main() {
	auto start = high_resolution_clock::now();
	int c = 0;
	int i = 2;
	vector<int> iFacts;
	int str = 0;
	while (c <= 4){
		iFacts = pFactorization(i);
		int nFacts = iFacts.size();
		if (nFacts == 4){
			str++;
		} else {
			str = 0;
		}
		if (str == 4){
			auto end = high_resolution_clock::now();
			auto dura = duration_cast<milliseconds>(end - start);
			cout << i - 3 << endl;
			cout << "Solution found in " << dura.count() << " milliseconds" << endl;
			return 0;
		}
		i++;
	}
}

vector<int> pFactorization(int n){
	vector<int> facts;
	while (n % 2 == 0){
		facts.push_back(2);
		n /= 2;
	}
	for (int i = 3; i <= sqrt(n); i += 2){
		while (n % i == 0){
			facts.push_back(i);
			n /= i;
		}
	}
	if (n > 2){
		facts.push_back(2);
	}
	vector<int>::iterator t;
	t = unique(facts.begin(), facts.end());
	facts.resize(distance(facts.begin(), t));
	return facts;
}
