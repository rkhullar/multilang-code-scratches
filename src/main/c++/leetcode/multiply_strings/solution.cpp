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
    digit operator[](const int) const;
    friend pointer operator+(const BigInteger &, const BigInteger &);
    friend pointer operator*(const BigInteger &, const BigInteger &);
    pointer partialMultiply(const digit, const int) const;
};

BigInteger::BigInteger(int size): digits(size) {};

int BigInteger::size() const {
    return digits.size();
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

digit BigInteger::operator[](const int index) const {
    // return nth digit from end
    const int n = digits.size();
    return 0 <= index && index < n ? digits.at(n - index -1) : 0;
}

BigInteger::pointer operator+(const BigInteger &self, const BigInteger &other) {
    const int size = max(self.size(), other.size());
    BigInteger::pointer result = BigInteger::from_size(size + 1);
    digit carry = 0;
    for(int index = 0; index < size; index++) {
        digit a = self[index];
        digit b = other[index];
        digit sum = a + b + carry;
        carry = sum / 10;
        result->digits.at(size - index) = sum % 10;
    }
    result->digits.at(0) = carry;
    return result;
}

BigInteger::pointer operator*(const BigInteger &self, const BigInteger &other) {
    const int size = other.size();
    BigInteger::pointer product = BigInteger::from_size(0);
    for(int index = 0; index < size; index++) {
        BigInteger::pointer addend = self.partialMultiply(other.digits[size - index - 1], index);
        product = *product + *addend;
    }
    return product;
}

BigInteger::pointer BigInteger::partialMultiply(const digit otherFactor, const int place) const {
    return BigInteger::from_size(0);
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