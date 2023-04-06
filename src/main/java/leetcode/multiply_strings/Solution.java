package leetcode.multiply_strings;

class BigInteger {

    final byte[] digits;

    BigInteger(int size) {
        digits = new byte[size];
    }

    public String toString() {
        StringBuilder builder = new StringBuilder();
        boolean wroteFirstDigit = false;
        for(byte digit: digits) {
            if(wroteFirstDigit || digit != 0) {
                builder.append(digit);
                wroteFirstDigit = true;
            }
        }
        if (!wroteFirstDigit)
            builder.append(0);
        return builder.toString();
    }

    static BigInteger fromString(String number) {
        int size = number.length();
        BigInteger result = new BigInteger(size);
        for(int i=0; i<size; i++) {
            char digitAsChar = number.charAt(i);
            byte digit = (byte) Integer.parseInt(digitAsChar+"");
            result.digits[i] = digit;
        }
        return result;
    }

    BigInteger multiply(BigInteger other) {
        BigInteger[] partial = this.partialMultiply(other);
        BigInteger total = new BigInteger(0);
        for(BigInteger addend: partial)
            total = total.plus(addend);
        return total;
    }

    BigInteger[] partialMultiply(BigInteger other) {
        BigInteger[] result = new BigInteger[other.digits.length];
        int size = other.digits.length;
        for(int i=0; i<size; i++)
            result[i] = this.partialMultiply(other.digits[size-i-1], i);
        return result;
    }

    BigInteger partialMultiply(byte other_factor, int place) {
        int size = this.digits.length;
        BigInteger result = new BigInteger( size + place + 1);
        byte carry = 0;
        for (int i=0; i<size; i++) {
            byte this_factor = this.digits[size-i-1];
            byte product = (byte) (this_factor * other_factor + carry);
            carry = (byte) (product / 10);
            result.digits[size-i] = (byte) (product % 10);
        }
        result.digits[0] = carry;
        return result;
    }

    BigInteger plus(BigInteger other) {
        return other;
    }
}

class Solution {
    public String multiply(String num1, String num2) {
        BigInteger a = BigInteger.fromString(num1);
        BigInteger b = BigInteger.fromString(num2);
        return a.multiply(b).toString();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String a = "123", b = "456";
        String product = solution.multiply(a, b);
        System.out.println(product);
//        BigInteger x = BigInteger.fromString(a);
//        System.out.println(x);
//        BigInteger t = x.partialMultiply((byte) 4, 2);
//        System.out.println(t);
    }
}
