/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const new_arr = []
    for(let i=0;i<nums.length;i++){
        for (let j=i+1;j<nums.length;j++){
            if (nums[i] + nums[j] === target){
                new_arr.push(i)
                new_arr.push(j)
            }
        }
    }
    return new_arr
};