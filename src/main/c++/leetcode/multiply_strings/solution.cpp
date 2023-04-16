using digit = unsigned char;

class BigInteger {

public:
    using pointer = unique_ptr<BigInteger>;

private:
    vector<digit> digits;

public:
    BigInteger(int size = 0);
    int size() const;
    static pointer from_size(int);
    static pointer from_string(string);
    friend string to_string(const BigInteger &);
    friend ostream& operator<<(ostream &, const BigInteger &);
    friend pointer operator+(const BigInteger &, const BigInteger &);
};

BigInteger::BigInteger(int size): digits(size) {};

int BigInteger::size() const {
    return this->digits.size();
}

BigInteger::pointer BigInteger::from_size(int size) {
    return make_unique<BigInteger>(size); // NOTE: added in c++ 14
}

BigInteger::pointer BigInteger::from_string(string number) {
    const int size = number.length();
    BigInteger::pointer result = BigInteger::from_size(size);
    for(int index = 0; index < size; index++) {
        result->digits.at(index) = (digit) (number[index] - '0');
    }
    return result;
}

string to_string(const BigInteger &self) {
    stringstream out; bool wroteFirstDigit = false;
    for(digit value: self.digits) {
        if(wroteFirstDigit || value != 0) {
            out << (char) (value + '0');
            wroteFirstDigit = true;
        }
    }
    if(!wroteFirstDigit) {
        out << 0;
    }
    return out.str();
}

ostream& operator<<(ostream &out, const BigInteger &self) {
    out << to_string(self);
    return out;
}

BigInteger::pointer operator+(const BigInteger &self, const BigInteger &other) {
    const int size = max(self.size(), other.size());
    BigInteger::pointer result = BigInteger::from_size(size + 1);
    digit carry = 0;
    for(int index = 0; index < size; index++) {
        digit a = self.digits.at(size - index - 1);
        digit b = other.digits.at(size - index - 1);
        digit sum = a + b + carry;
        carry = sum / 10;
        result->digits.at(size - index) = sum % 10;
    }
    result->digits.at(0) = carry;
    return result;
}

class Solution {
public:
    string multiply(string num1, string num2) {
        BigInteger::pointer a = BigInteger::from_string(num1);
        BigInteger::pointer b = BigInteger::from_string(num2);
//        return to_string(*a);
        return "0";
    }
};