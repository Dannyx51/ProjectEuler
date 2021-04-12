#include <iostream>
#include <chrono>

using namespace std;
using namespace chrono;

int sequenceLength(int num){
	int base = 1 % num;
	int l = 1;
	int mod = (base * 10) % num;
	while (mod != base){
		mod = (mod * 10) % num;
		l++;
	}
	return l;
}


int main() {
	/*
	Theres a little trick I found because decimals make me want to die, 
	(especially the long variety)
	Important rule 1/d's length max = d - 1
	If you take your number, lets say seven: 1/7
	take 1 % 7 == 1
	then multuply the numerator by 10 until you get the first modulo answer, in our case, 1
	ex:
	1 % 7 = 1
	10 % 7 = 3
	20 % 7 = 6
	30 % 7 = 4
	40 % 7 = 5
	50 % 7 = 1
	Note you include the index that is a repeat!
	1 % 7 has a sequence length of 6, the max for that number (6)
	*/
	auto start = high_resolution_clock::now();
	int longest = 0;
	int n;
	int l = 0;
	for (int i = 1; i < 1000; i+=2){
		if (i % 5 != 0){
			l = sequenceLength(i);
			if (l > longest){
				longest = l;
				n = i;
			}
			//cout << i << ": " << l << endl;
		}
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<microseconds>(end - start);
	cout << n << " has the longest: " << longest << endl;
	cout << "Soulution found in " << dura.count() << " microseconds" << endl;
}
