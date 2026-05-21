class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let arr = new Array(26).fill(0)

        if(s.length != t.length)
            return false

        
        // Flag letters with 1
        for(const c of s){
            arr[c.charCodeAt(0)-97]++
        }

        // Flag letters with -1
        for(const c of t){
            arr[c.charCodeAt(0)-97]--
        }

        let na = arr.find((i) => i!=0);

        
        return na == undefined
    }
}