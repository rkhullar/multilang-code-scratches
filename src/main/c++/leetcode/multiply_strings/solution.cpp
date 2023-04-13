typedef unsigned char byte;

class BigInteger {

private:
    byte *digits;

public:
    BigInteger(int size = 0);
    int length();

//    string to_string() {
//        return "BI";// + size();
//    }
};

BigInteger::BigInteger(int size) {
    this->digits = new byte[size];
}

int BigInteger::length() {
    return sizeof(this->digits);
}

class Solution {
public:
    string multiply(string num1, string num2) {
        return "0";
    }
};


/*
class BigInt {
  final private byte[] digits;
  Person(int size) {
  this.digits = new byte[size];
  }

  int size() {
  return this.digits.length();
  }
}
*/