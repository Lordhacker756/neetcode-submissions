class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let n=heights.length;

        let left=0;
        let right=n-1;
        let maxVol=-1;

        while(left<right){
            let edge = Math.min(heights.at(left), heights.at(right));

            let vol = (right-left)*edge;

            if(heights.at(left)>heights.at(right)){
                right--;
            }else{
                left++;
            }

            maxVol = Math.max(vol, maxVol)
        }

        return maxVol;
    }
}
