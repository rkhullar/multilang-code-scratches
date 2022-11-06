package leetcode.add_two_numbers;


// * Definition for singly-linked list.

class ListNode {
int val;
  ListNode next;
  ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
class MyList {
    ListNode head = null, tail = null;
    int size = 0;

    void add(int item) {
        ListNode node = new ListNode(item);
        if(head == null || tail == null) {
            head = node; tail = node; size++;
        } else {
            tail.next = node; size++; tail = node;
        }
    }

    void print() {
        ListNode curr = head;
        while(curr != null) {
            System.out.println(curr.val);
            curr = curr.next;
        }
    }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int total = 0, carry = 0;
        MyList result = new MyList();
        while(l1 != null && l2 != null) {
            int partial = l1.val + l2.val + carry;
            total = partial % 10; carry = partial / 10;
            result.add(total);
            l1 = l1.next; l2 = l2.next;
        }
        while(l1 != null) {
            int partial = l1.val + carry;
            total = partial % 10; carry = partial / 10;
            result.add(total);
            l1 = l1.next;
        }
        while(l2 != null) {
            int partial = l2.val + carry;
            total = partial % 10; carry = partial / 10;
            result.add(total);
            l2 = l2.next;
        }
        if(carry > 0)
            result.add(carry);
        return result.head;
    }

    public static void main(String[] args) {
        // 342 + 465 => 807

        ListNode a =  new ListNode(2, new ListNode(4, new ListNode(3)));
        ListNode b =  new ListNode(5, new ListNode(6, new ListNode(4)));
        ListNode s = new Solution().addTwoNumbers(a, b);

        MyList dut = new MyList();
        dut.head = s;
        dut.print();
    }
}
