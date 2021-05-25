#include <iostream>
#inlcude <chrono>

using namespace std;
using namespace chrono;

long lTen(int a, int b);

int main()
{
  auto start = high_resolution_clock::now();
	long s = 0;
	for (int i = 1; i < 1001; i++){
		s += lTen(i, i);
		string str = to_string(s);
		if (str.length() > 10){
			str = str.substr(str.length() - 10);
		}
		s = stol(str);
	}
  auto end = high_resolution_clock::now();
  auto dura = duration_cast<microseconds>(end - start);
	cout << s << endl;
  cout << "Solution found in " << dura.count() << " microseconds" << endl;
}

long lTen(int a, int b){
	unsigned long long n = 1;
	for (int i = 0; i < b; i++){
		n *= a;
		string str = to_string(n);
		if (str.length() > 10){
			str = str.substr(str.length() - 10);
		}
		n = stol(str);
		if (i == b - 1){
			return stol(str);
		}
	}
	return 0;
}
