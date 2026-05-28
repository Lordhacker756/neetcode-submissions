class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = [];

        let hash = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        if(s.length==1){
            return false;
        }

        for(let i=0; i< s.length; i++){
            let curr = s[i]; 

            if(hash[curr] !== undefined){ //it's a opening bracket
                // push to stack
                stack.push(curr)
            }else{
                let last = stack.pop(); // Pop the last open bracket
                if(hash[last] !== curr){ //the current item must be the closing bracket 
                    return false;
                }
            }
        }


        if(stack.length==0)
        return true;

        return false;
    }
}
