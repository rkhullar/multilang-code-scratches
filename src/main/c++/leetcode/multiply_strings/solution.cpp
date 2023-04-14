using digit = unsigned char;

class BigInteger {

public:
    using pointer = unique_ptr<BigInteger>;

private:
    vector<digit> digits;

public:
    BigInteger(int size = 0);
    const int size();
    static pointer from_string(string);
    friend ostream& operator<<(ostream &, const BigInteger &);
};

BigInteger::BigInteger(int size): digits(size) {};

const int BigInteger::size() {
    return this->digits.size();
}

BigInteger::pointer BigInteger::from_string(string number) {
    BigInteger::pointer result (new BigInteger(5));
    return result;
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