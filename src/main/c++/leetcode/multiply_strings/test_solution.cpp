void test_array() {
    const int n = 4;
    int *dut = new int[n];
    // note: cannot get size from pointer?
    for(int i=0; i<n; i++) {
        dut[i] = i*3+40;
        cout << dut[i] << endl;
    }
    delete[] dut;
}

void test_vector() {
    // originally read from argv[1]
    const int n = stoi("4");
    cout << n << endl;

    vector<int> dut(n);
    cout << dut.size() << endl;
    for(int i=0; i<dut.size(); i++) {
        dut.at(i) = i*2+20;
        cout << dut.at(i) << endl;
    }
}

int main(int argc, char *argv[]) {
//    string a = "123", b = "456";
//    cout << a << endl;
//    cout << b << endl;
//    Solution solution;
//    string result = solution.multiply(a, b);
//    cout << result << endl;

    BigInteger::pointer a = BigInteger::from_string("123");
    BigInteger::pointer b = BigInteger::from_string("456");
//    cout << a->size() << endl;
//    cout << *a << endl;

    BigInteger::pointer c = *a + *b;
    cout << *c << endl;

    return 0;
}

// scraps
/* - before delegated constructor
BigInteger::BigInteger(int size) {
    vector<digit> digits(size);
    this->digits = digits;
}
*/

/* - before make_unique
BigInteger::pointer result(new BigInteger(size));
return result;
*/
