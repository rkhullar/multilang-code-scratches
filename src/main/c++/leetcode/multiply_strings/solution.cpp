typedef unsigned char digit;

class BigInteger {

private:
    digit *digits;
    int _size;

public:
    BigInteger(int size = 0);
    ~BigInteger();
    const int size();
    friend ostream& operator<<(ostream &, const BigInteger &);

//    string to_string() {
//        return "BI";// + size();
//    }
};

BigInteger::BigInteger(int size) {
    this->digits = new digit[size];
    this->_size = size;
}

BigInteger::~BigInteger() {
    delete[] this->digits;
}

const int BigInteger::size() {
    return this->_size;
}

ostream& operator<<(ostream &out, const BigInteger &self) {
    out << self._size;
    return out;
}

class Solution {
public:
    string multiply(string num1, string num2) {
        return "0";
    }
};