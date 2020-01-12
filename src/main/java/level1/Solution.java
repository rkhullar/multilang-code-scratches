package level1;

public class Solution {

    // Fibonacci Number
    public static int fib(int n) {
        return recursiveFibonacci(n);
    }

    public static int recursiveFibonacci(int n) {
        if (n == 0 || n == 1)
            return  n;
        else
            return fib(n-1) + fib(n-2);
    }

    // Find the Missing Number in a Set of Numbers from 1 to 10
    public static int sum_1toN(int n) {
        return (n + 1) * n / 2;
    }

    public static int findMissingNumber(int[] arr) {
        final int sum_10 = sum_1toN(10);
        int sum_arr = 0;
        for (int x: arr)
            sum_arr += x;
        return sum_10 - sum_arr;
    }

    // Delete a List's Head Node
    public static ListNode deleteAtHead(ListNode head) {
        if (head != null) {
            ListNode curr = head.next;
            head.next = null;
            return curr;
        } else {
            return null;
        }
    }

    // Insert a Node at the End of a Linked List
    public static ListNode insertAtTail(ListNode head, int data) {
        ListNode curr = head, node = new ListNode(data);
        while (curr != null && curr.next != null)
            curr = curr.next;
        if (curr == null)
            return node;
        else {
            curr.next = node;
            return head;
        }
    }

    // Find the Middle of a List in a Single Pass
    public static ListNode findMiddleNode(ListNode head) {
        ListNode slow_curr = head, fast_curr = head;
        while (slow_curr != null && fast_curr != null)
        {
            fast_curr = fast_curr.next;
            if (fast_curr != null && fast_curr.next != null)
                fast_curr = fast_curr.next;
            else
                break;
            slow_curr = slow_curr.next;
        }
        return slow_curr;
    }

}
