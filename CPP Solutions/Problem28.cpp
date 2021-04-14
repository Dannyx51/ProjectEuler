#include <iostream>

using namespace std;

int main() {
  int l = 1001 * 1001;
	int total = 0;
	int index = 0;
	int inc = 2;
	int c = 1;
	while (index < l){
		total += index + 1;
		index += inc;
		if (c == 4){
			inc += 2;
			c = 0;
		}
		c++;
	}
	cout << total << endl;
}
