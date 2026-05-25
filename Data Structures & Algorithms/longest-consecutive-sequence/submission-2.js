class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
    let s = new Set(nums);
    let n = nums.length;
    let res=-1;

    if(nums.length == 0){
        return 0;
    }


    s.forEach((currNum)=>{
        let currCount = 1;

        if(s.has(currNum-1)){
        }else {
            // Start of a sequence
            while(s.has(currNum+1)){
                currNum++;
                currCount++;
            }
        }

        res = Math.max(res, currCount);
    });

    return res;

    }}
