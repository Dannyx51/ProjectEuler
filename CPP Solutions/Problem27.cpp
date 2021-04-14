#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <chrono>

using namespace std;
using namespace chrono;

bool isPrime(int n){
	for (int i = 2; i < sqrt(n) + 1; i++){
		if (n % i == 0){
			return false;
		}
	}
	return true;
}
int main(){
	auto start = high_resolution_clock::now();
	vector<int> prime;
	vector<int> arr;
	prime.push_back(2);
	arr.push_back(2);
	for (int i = 2; i < 1000; i++){
		if (isPrime(i)){
			prime.push_back(i);
		}
	}
	int m = 0;
	int prod;
	for (int a : prime){
		for (int b : prime){
			//cout << a << " - " << b << endl;
			int n = 0;
			while (true){
				int f = (n * n) + (a * n) + b;
				if (find(prime.begin(), prime.end(), f) == prime.end()){
					if (isPrime(f)){
						arr.push_back(f);
					} else {
						if (n - 1 > m){
							m = n - 1;
							prod = a * b;
						}
						break;
					}
				}
				n++;
			}
			n = 0;
			while (true){
				int f = (n * n) - (a * n) + b;
				if (find(prime.begin(), prime.end(), f) == prime.end()){
					if (isPrime(abs(f))){
						arr.push_back(f);
					} else {
						if (n - 1 > m){
							m = n - 1;
							prod = a * b;
						}
						break;
					}
				}
				n++;
			}
		}
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<milliseconds>(end - start);
	cout << prod * -1 << endl;
	cout << "Solution found in " << dura.count() << " milliseconds" << endl;
}
