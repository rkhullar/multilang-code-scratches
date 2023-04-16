package leetcode.multiply_strings;

class BigInteger {

    private final byte[] digits;

    BigInteger(int size) {
        digits = new byte[size];
    }

    public String toString() {
        StringBuilder builder = new StringBuilder();
        boolean wroteFirstDigit = false;
        for (byte digit: digits) {
            if(wroteFirstDigit || digit != 0) {
                builder.append(digit);
                wroteFirstDigit = true;
            }
        }
        if (!wroteFirstDigit)
            builder.append(0);
        return builder.toString();
    }

    public static BigInteger fromString(String number) {
        int size = number.length();
        BigInteger result = new BigInteger(size);
        for (int i=0; i<size; i++) {
            char digitAsChar = number.charAt(i);
            byte digit = (byte) Integer.parseInt(digitAsChar+"");
            result.digits[i] = digit;
        }
        return result;
    }

    public BigInteger multiply(BigInteger other) {
        return this.multiply_v2(other);
    }

    private BigInteger multiply_v1(BigInteger other) {
        BigInteger[] partial = this.partialMultiply(other);
        BigInteger total = new BigInteger(0);
        for (BigInteger addend: partial)
            total = total.plus(addend);
        return total;
    }

    private BigInteger multiply_v2(BigInteger other) {
        // space optimized
        int size = other.digits.length;
        BigInteger product = new BigInteger(0);
        for (int i=0; i<size; i++) {
            BigInteger addend = this.partialMultiply(other.digits[size-i-1], i);
            product = product.plus(addend);
        }
        return product;
    }

    private BigInteger[] partialMultiply(BigInteger other) {
        int size = other.digits.length;
        BigInteger[] result = new BigInteger[size];
        for (int i=0; i<size; i++)
            result[i] = this.partialMultiply(other.digits[size-i-1], i);
        return result;
    }

    private BigInteger partialMultiply(byte other_factor, int place) {
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

    public BigInteger plus(BigInteger other) {
        int size = Math.max(this.digits.length, other.digits.length);
        BigInteger result = new BigInteger(size + 1);
        byte carry = 0;
        for (int i=0; i<size; i++) {
            byte a = this.digitAt(i);
            byte b = other.digitAt(i);
            byte sum = (byte) (a + b + carry);
            carry = (byte) (sum / 10);
            result.digits[size-i] = (byte) (sum % 10);
        }
        result.digits[0] = carry;
        return result;
    }

    private byte digitAt(int index) {
        // return nth digit from end
        final int size = this.digits.length;
        if (0 <= index && index < size)
            return this.digits[size - index - 1];
        return 0;
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
    }
}
