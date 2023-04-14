typedef unsigned char digit;

class BigInteger {

private:
    vector<digit> digits;

public:
    BigInteger(int size = 0);
    const int size();
    friend ostream& operator<<(ostream &, const BigInteger &);
};

BigInteger::BigInteger(int size): digits(size) {};

/*
BigInteger::BigInteger(int size) {
    vector<digit> digits(size);
    this->digits = digits;
}
*/

const int BigInteger::size() {
    return this->digits.size();
}

ostream& operator<<(ostream &out, const BigInteger &self) {
    out << self.digits.size();
    return out;
}

class Solution {
public:
    string multiply(string num1, string num2) {
        return "0";
    }
};