#include <iostream>

using namespace std;

int ones(int num);
int tens(int num);
int hunds(int num);

int main() {
	//21124
	int total = 0;
	int l;
	for (int i = 1; i <= 1000; i++){
		l = to_string(i).length();
		if (i == 1000){
			total += 11;
		} else if (l == 1){
			total += ones(i);
		} else if (l == 2){
			total += tens(i);
		} else {
			total += hunds(i);
		}
	}
	cout << total << endl;
}

int ones(int num){
	if ((num > 0 && num < 3) || num == 6){
		return 3;
	} else if (num == 4 || num == 5 || num == 9){
		return 4;
	} else if (num == 0){
		return 0;
	} else {
		return 5;
	}
}

int tens(int num){
	int o = 0;
	int t = 0;
	if (to_string(num).length() == 1){
		return ones(num);
	} else {
		o = stoi(to_string(num).substr(1,1));
		t = stoi(to_string(num).substr(0,1));
	}

	if (num < 20){
		if (num == 11 || num == 12){
			return 6;
		} else if (num == 15 || num == 16){
			return 7;
		} else if (num == 13 || num == 14 || num == 18 || num == 19){
			return 8;
		} else if (num == 10){
			return 3;
		} else {
			return 9;
		}
	} else {
		if (t == 2 || t == 3 || t == 8 || t == 9){
			return 6 + ones(o);
		} else if (t == 6 || t == 4 || t == 5){
			return 5 + ones(o);
		} else {
			return 7 + ones(o);
		}
	}
}

int hunds(int num){
	int h = stoi(to_string(num).substr(0,1));
	int to = stoi(to_string(num).substr(1,2));
	if (to == 0){
		return ones(h) + 7;
	} else {
		return ones(h) + tens(to) + 10;
	}
}
