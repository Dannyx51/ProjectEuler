#include <iostream>
#include <math.h>
#include <string>
#include <chrono>

using namespace std;
using namespace chrono;

bool isPrime(long long n);

bool pLeft(string str);
bool pRight(string str);

int main() {
	auto start = high_resolution_clock::now();
	long long n = 11;
	int c = 1;
	int s = 0;
	while (c <= 11){
		if (n % 5 == 0 || n % 2 == 0){
			n += 2;
			continue;
		}
		if (isPrime(n)){
			if (pLeft(to_string(n)) && pRight(to_string(n))){
				s += n;
				c++;
			}
		}
		n += 2;
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<milliseconds>(end - start);
	cout << s << endl;
	cout << "Solution found in " << dura.count() << " milliseconds" << endl;
}

bool isPrime(long long n){
	if (n == 1){
		return false;
	}
	if (n == 2){
		return true;
	}
	if (n % 2 == 0){
		return false;
	}
	for (long long i = 3; i < sqrt(n) + 1; i++){
		if (n % i == 0){
			return false;
		}
	}
	return true;
}

bool pLeft(string str){
	while (str.length() > 1){
		str.erase(str.begin());
		if (!isPrime(stoll(str))){
			return false;
		}
	}
	return true;
}

bool pRight(string str){
	while (str.length() > 1){
		str.erase(str.end() - 1);
		if (!isPrime(stoll(str))){
			return false;
		}
	}
	return true;
}
