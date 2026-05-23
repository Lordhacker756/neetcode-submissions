class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs) {
        let res="";
        let n=strs.length;
        let min_len = Number.MAX_VALUE;

        strs.forEach((word)=>{
            if(word.length < min_len){
                min_len = word.length
            }
        })

        for(let i=0; i<min_len; i++){
            let currChar="";
            for(let j=0;j<n; j++){
                let word = strs[j];

                if(j==0){
                    currChar=word[i];
                }else{
                    if(currChar != word[i]){
                        return res;
                    }
                }
            }
            res+=currChar;
        }

        return res;
    }
}
