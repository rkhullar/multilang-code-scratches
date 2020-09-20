package firecode.level1;

public class ListNode<T> {
    T data;
    ListNode<T> prev;
    ListNode<T> next;

    ListNode(T data) {
        this.data = data;
    }

    boolean hasPrev() {
        return prev != null;
    }

    boolean hasNext() {
        return next != null;
    }

    static <T> ListNode<T> from(T... args) {
        ListNode<T> nodes[] = new ListNode[args.length];
        for(int i=0; i<args.length; i++)
            nodes[i] = new ListNode<>(args[i]);
        for(int i=0; i<args.length-1; i++) {
            nodes[i].next = nodes[i+1];
            nodes[i+1].prev = nodes[i];
        }
        return nodes[0];
    }

    int size() {
        int count = 0;
        for(ListNode<T> curr = this; curr != null; curr = curr.next, count++);
        return count;
    }

    void readInto(T[] arr) {
        ListNode<T> curr = this; int idx = 0;
        while(curr != null && idx < arr.length) {
            arr[idx++] = curr.data;
            curr = curr.next;
        }
    }

    @SuppressWarnings("unchecked")
    T[] toArray() {
        final int n = this.size();
        final T[] arr = (T[]) new Object[n];
        this.readInto(arr);
        return arr;
    }
}