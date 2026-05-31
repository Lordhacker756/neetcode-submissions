class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l=0, h=nums.length-1;


        while(l<=h){ //should be l<=h not l<h
            let mid = Math.floor((h+l)/2);
            console.log(l,mid,h)
            if(nums[mid] == target) return mid;

            if(nums[l] <= nums[mid]){
                // left side is sorted
                if(target >= nums[l] && target < nums[mid]){
                    h=mid-1
                }else{
                    l=mid+1
                }
            }else {
                // right side is sorted
                if(target > nums[mid] && target <= nums[h]){
                    l=mid+1
                }else{
                    h=mid-1
                }
            }
        }

        return -1;
    }
}
