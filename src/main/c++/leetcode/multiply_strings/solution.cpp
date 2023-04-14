typedef unsigned char digit;

class BigInteger {

private:
    digit *digits;
    int _size;

public:
    BigInteger(int size = 0);
    int size();

//    string to_string() {
//        return "BI";// + size();
//    }
};

BigInteger::BigInteger(int size) {
    this->digits = new digit[size];
    this->_size = size;
}

int BigInteger::size() {
    return this->_size;
}

class Solution {
public:
    string multiply(string num1, string num2) {
        return "0";
    }
};