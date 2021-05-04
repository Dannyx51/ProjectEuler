#include <iostream>
#include <cmath>
#include <chrono>

using namespace std;
using namespace chrono;

int main() {
	auto start = high_resolution_clock::now();
	//Perimeter loop
	int b = 0;
	int bigP;
	for (int p = 3; p <= 1000; p++){
		int pNum = 0;
		for (int a = 1; a < p; a++){
			for (int b = 1; b < p ; b++){
				int c = sqrt((a * a) + (b * b));
				if (b != c){
					if (a != c){
						if (a + b + c == p){
							if ((c * c) == (a * a) + (b * b)){
								if (a < b && b < c){
									pNum++;
								}
							}
						}
					}
				}
			}
		}
		if (b < pNum){
			b = pNum;
			bigP = p;
		}
		//cout << p << ": " << pNum << endl;
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<seconds>(end - start);
	cout << bigP;
	cout << "Solution found in " << dura.count() << " seconds" << endl; 
}
