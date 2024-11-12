/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let new_arr = [...nums1, ...nums2];
    new_arr.sort((a, b) => a - b);
    const len = new_arr.length;

    if (len % 2 === 0) {
        const mid1 = Math.floor(len / 2) - 1;
        const mid2 = mid1 + 1;
        return (new_arr[mid1] + new_arr[mid2]) / 2;
    } else {
        const mid = Math.floor(len / 2);
        return new_arr[mid];
    }
};