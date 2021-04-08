#include <iostream>
#include <array>
#include <chrono>
using namespace ::std;
using namespace chrono;
int main() {
    auto start = high_resolution_clock::now();
    int num1, num2, num3;
    num3 = 0;
    num1 = num2 = 1;

    int max = 4000000;
    int sum = 0;
    while (num3 < max) {
        num3 = num1 + num2;
        num1 = num2;
        num2 = num3;
        if (num3 % 2 == 0) {
            sum += num3;
        }
    }
    auto end = high_resolution_clock::now();
    auto diff = duration_cast<nanoseconds>(end - start);
    //Had to use nano seconds because too fast
    cout << sum << " Solution found in " << diff.count() << " nanoseconds " << endl;
    return 0;
}
