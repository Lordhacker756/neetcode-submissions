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

        
        for(let i = 0; i<s.length; i++){
            arr[s[i].charCodeAt(0)-97]++
            arr[t[i].charCodeAt(0)-97]--

        }

        let na = arr.find((i) => i!=0);

        console.log(arr)        
        return na == undefined
    }
}