using digit = unsigned char;

class BigInteger {

public:
    using pointer = unique_ptr<BigInteger>;

private:
    vector<digit> digits;

public:
    BigInteger(int size = 0);
    const int size();
    static pointer from_size(int);
    static pointer from_string(string);
    friend string to_string(const BigInteger &);
    friend ostream& operator<<(ostream &, const BigInteger &);
    friend pointer operator+(const BigInteger &, const BigInteger &);
};

BigInteger::BigInteger(int size): digits(size) {};

const int BigInteger::size() {
    return this->digits.size();
}

BigInteger::pointer BigInteger::from_size(int size) {
    return make_unique<BigInteger>(size); // NOTE: added in c++ 14
}

BigInteger::pointer BigInteger::from_string(string number) {
    const int size = number.length();
    BigInteger::pointer result = BigInteger::from_size(size);
    for(int index=0; index < size; index++) {
        result->digits.at(index) = (digit) (number[index] - '0');
    }
    return result;
}

string to_string(const BigInteger &self) {
    stringstream out;
    const int size = self.digits.size();
    for(int index=0; index < size; index++) {
        out << (char) (self.digits.at(index) + '0');
    }
    return out.str();
}

ostream& operator<<(ostream &out, const BigInteger &self) {
    out << to_string(self);
    return out;
}

BigInteger::pointer operator+(const BigInteger &self, const BigInteger &other) {
    return nullptr;
}

class Solution {
public:
    string multiply(string num1, string num2) {
        return "0";
    }
};