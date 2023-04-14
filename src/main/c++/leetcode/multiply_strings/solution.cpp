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
    const int size = number.length();
    BigInteger::pointer result(new BigInteger(size));
    for(int index=0; index < size; index++) {
        result->digits.at(index) = 1 + '0';
    }
    return result;
}

ostream& operator<<(ostream &out, const BigInteger &self) {
    const int size = self.digits.size();
    for(int index=0; index < size; index++) {
        out << self.digits.at(index);
    }
    return out;
}

class Solution {
public:
    string multiply(string num1, string num2) {
        return "0";
    }
};