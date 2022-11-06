package leetcode.add_two_numbers_2;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    private int listSize(ListNode head) {
        ListNode curr = head; int size = 0;
        while(curr != null) {
            curr = curr.next; size++;
        }
        return size;
    }

    private void listToArr(ListNode head, int[] arr, int start) {
        ListNode curr = head;
        for(int i=start; curr!=null && i<arr.length; i++) {
            arr[i] = curr.val;
            curr = curr.next;
        }
    }

    private ListNode arrToList(int[] arr) {
        ListNode curr = null, head = null;
        for(int i=0; i<arr.length; i++) {
            ListNode node = new ListNode(arr[i]);
            if(curr != null) {
                curr.next = node;
                curr = curr.next;
            } else {
                if(arr[i] > 0 || i == arr.length-1) {
                    curr = node;
                    head = curr;
                }
            }
        }
        return head;
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int size1 = listSize(l1), size2 = listSize(l2);
        int size = (size1 > size2 ? size1 : size2) + 1;
        int[] arr1 = new int[size], arr2 = new int[size];
        listToArr(l1, arr1, size-size1); listToArr(l2, arr2, size-size2);

        int[] carry = new int[size];
        int[] sum = new int[size];
        for(int i=size-1; i>0; i--) {
            int partial = arr1[i] + arr2[i] + carry[i];
            sum[i] = partial % 10; carry[i-1] = partial / 10;
        }
        sum[0] = carry[0];

        return arrToList(sum);
    }
}