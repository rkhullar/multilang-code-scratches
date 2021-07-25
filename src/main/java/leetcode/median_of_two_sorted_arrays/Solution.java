package leetcode.median_of_two_sorted_arrays;

class Solution {

    public int[] merge(int[] a, int[] b) {
        final int m = a.length, n = b.length;
        int[] result = new int[m + n];
        int i = 0, j = 0, k = 0;
        while(i < m && j < n) {
            if (a[i] < b[j])
                result[k++] = a[i++];
            else
                result[k++] = b[j++];
        }
        while(i < m)
            result[k++] = a[i++];
        while(j < n)
            result[k++] = b[j++];
        return result;
    }

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] merged = this.merge(nums1, nums2);
        int mid_idx = merged.length / 2;
        if (merged.length % 2 == 1)
            return merged[mid_idx];
        else
            return (merged[mid_idx - 1] + merged[mid_idx]) / 2.0;
    }
}