#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <chrono>
using namespace std;
using namespace chrono;
string add(string num1, string num2);
string mult(string num1, string num2);
string pow(string num1, int num2);
vector<string> remDupe(vector<string> arr);

int main() {
	auto start = high_resolution_clock::now();
	int l = 0;
	vector<string> arr;
	for (int i = 100; i >= 2; i--){
		for (int ii = 100; ii >= 2; ii--){
			arr.push_back(pow(to_string(i), ii));
		}
		cout << i << endl;
	}
	arr = remDupe(arr);
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<seconds>(end - start);
	cout << arr.size() << endl;
	cout << "Solution found in " << dura.count() << " seconds" << endl;
}

string add(string a, string b){
	if (a.length() < b.length()){
		string temp = a;
		a = b;
		b = temp;
	}
	int diff = a.length() - b.length();
	int r = 0;
	string tot = "";
	for (int i = a.length() - 1; i >= 0; i--){
		int n1 = stoi(a.substr(i, 1));
		int n2;
		if (i - diff > b.length()){
			n2 = 0;
		} else {
			n2 = stoi(b.substr(i - diff, 1));
		}
		int t = n1 + n2 + r;
		if (t < 10){
			tot = to_string(t) + tot;
			r = 0;
		} else {
			r = stoi(to_string(t).substr(0, 1));
			t = stoi(to_string(t).substr(1, 1));
			tot = to_string(t) + tot;
		}
	}
	if (r > 0){
		tot = to_string(r) + tot;
	}
	return tot;
}
string mult(string a, string b){
	if (a.length() > b.length()){
		string temp = a;
		a = b;
		b = temp;
	}
	int diff = a.length() - b.length();
	int r = 0;
	string str = "0";
	int z = 0;
	for (int i = a.length() - 1; i >= 0; i--){
		string tot = "";
		for (int iii = 0; iii < z; iii++){
			tot = tot + "0";
		}
		for (int ii = b.length() - 1; ii >= 0; ii--){
			int n1 = stoi(a.substr(i, 1));
			int n2 = stoi(b.substr(ii , 1));
			int t = (n1 * n2) + r;
			if (t < 10){
				tot = to_string(t) + tot;
				r = 0;
			} else {
				r = stoi(to_string(t).substr(0, 1));
				t = stoi(to_string(t).substr(1, 1));
				tot = to_string(t) + tot;
			}
		}
		if (r > 0){
			tot = to_string(r) + tot;
			r = 0;
		}
		str = add(str, tot);
		z++;
	}
	return str;
}

string pow(string b, int n){
	string tot = b;
	for (int i = 1; i < n; i++){
		tot = mult(tot, b);
	}
	return tot;
}

vector<string> remDupe(vector<string> vec){
	sort( vec.begin(), vec.end() );
	vec.erase( unique( vec.begin(), vec.end() ), vec.end() );
	return vec;
}
