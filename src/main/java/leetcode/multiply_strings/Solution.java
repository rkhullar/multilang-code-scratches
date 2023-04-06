package leetcode.multiply_strings;

class BigInteger {

    final byte[] digits;

    BigInteger(int size) {
        digits = new byte[size];
    }

    public String toString() {
        StringBuilder builder = new StringBuilder();
        for(byte digit: digits)
            builder.append(digit);
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
}

class Solution {
    public String multiply(String num1, String num2) {
        return "";
    }

    public static void main(String[] args) {
        String a = "123", b = "456";
        BigInteger x = BigInteger.fromString(a);
        System.out.println(x);
    }
}
