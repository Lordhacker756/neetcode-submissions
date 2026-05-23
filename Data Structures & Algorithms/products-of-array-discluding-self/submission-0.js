class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let res = [];
        let pp = [];
        let sp = [];
        let n = nums.length;

        // prefix pdt
        // 1, 1, 2, 8
        for(let i=0; i<n; i++){
            if(i==0){
                pp.push(1)
            }else if(i==1){
                pp.push(nums[i-1])
            }else{
                pp.push(nums[i-1]*pp[i-1])
            }
        }

        // suffix pdt
        for(let i=n-1; i>=0; i--){
            if(i==n-1){
                sp[i] = 1;
            }else{
                sp[i] = nums[i+1] * sp[i+1];
            }
        }

        for(let i=0; i<n;i++){
            res.push(pp[i]*sp[i])
        }

        return res;
    }
}
