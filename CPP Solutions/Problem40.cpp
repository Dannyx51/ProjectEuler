#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace chrono;

int main() {
	auto start = high_resolution_clock::now();
	string str = "";
	for (int i = 1; i < 1000001; i++){
		str += to_string(i);
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<milliseconds>(end - start);
	cout << (int(str[0]) - 48) * (int(str[9]) - 48) * (int(str[99]) - 48) * (int(str[999]) - 48) * (int(str[9999]) - 48)  * (int(str[99999] - 48)) * (int(str[999999]) - 48) << endl;
	cout << "Solution found in " << dura.count() << " milliseconds" << endl;
}
