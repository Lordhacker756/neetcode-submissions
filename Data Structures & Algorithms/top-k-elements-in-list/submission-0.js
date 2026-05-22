class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {

    let mp = new Map()
    let res = Array.from({ length: nums.length+1 }, () => [])
    let resf = []

    // hash map of number and it's frequency
    nums.forEach(item => {
        if(mp.has(item)){
            let prevFreq = mp.get(item)
            mp.set(item, prevFreq+=1)
        }else{
            mp.set(item, 1)
        }
    })

    for(let [key, value] of mp.entries()){
        res[value].push(key)
    }
    
    

    for(let i=res.length-1; i>=0; i--){ //0
        let items = res[i] //[1]
        for(let j=0; j<items.length; j++){
        if(resf.length < k){
            resf.push(items[j])
        }
        }
    }
    
    return(resf)
    }
}
