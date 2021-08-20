#include <iostream>
#include <chrono>
using namespace ::std;
using namespace chrono;
int main() {
    auto start = high_resolution_clock::now();
    int sum = 0;
    for (int i = 1; i < 1000; i++) {
        if (i % 3 == 0) {
            sum += i;
        }
        else if (i % 5 == 0) {
            sum += i;
        }
    }
    auto end = high_resolution_clock::now();
    auto diff = duration_cast<nanoseconds>(end - start);
    cout << sum << " Solution found in " << diff.count() << " nanoseconds " << endl;
    return 0;
}
