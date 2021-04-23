#include <iostream>
#include <chrono>
#include <vector>
#include <math.h>

using namespace std;
using namespace chrono;

vector<int> genPrimes(int n);
bool isPrime(int n);
bool rotate(int p);

int main() {
	auto start = high_resolution_clock::now();
	int n = 1; //We dont check the primality of 2
	vector<int> p = genPrimes(1000000);
	for (int i = 0; i < p.size(); i++){
		if (rotate(p.at(i))){
			n++;
		}
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<seconds>(end - start);
	cout << n << endl;
	cout << "Solution found in " << dura.count() << " seconds" << endl;
}

vector<int> genPrimes(int n){
	vector<int> p;
	for (int i = 3; i < n; i += 2){
		if (isPrime(i)){
			p.push_back(i);
		}
	}
	return p;
}

bool isPrime(int n){
	for (int i = 2; i < sqrt(n) + 1; i++){
		if (n % i == 0){
			return false;
		}
	}
	return true;
}

bool rotate(int p){
	string str = to_string(p);
	string arr[str.length()];

	for (int i = 0; i < str.length(); i++){
		arr[i] = str.substr(i, 1);
	}
	int n = sizeof(arr) / sizeof(arr[0]);
	for (int i = 0; i < str.length() - 1; i++){
		string temp = arr[0];
		for (int i = 0; i < n - 1; i++){
			arr[i] = arr[i + 1];
		}
		arr[n - 1] = temp;
		string con;
		for (int i= 0; i < n; i++){
			con += arr[i];
		}
		if (!isPrime(stoi(con))){
			return false;
		}
	}
	return true;
}
