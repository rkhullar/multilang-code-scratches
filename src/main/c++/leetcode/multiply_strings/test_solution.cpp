#include <iostream>
#include "solution.h"

using namespace std;

int main()
{
    string a = "123", b = "456";
    cout << a << endl;
    cout << b << endl;
    Solution solution;
    string result = solution.multiply(a, b);
    cout << result << endl;
    return 0;
}