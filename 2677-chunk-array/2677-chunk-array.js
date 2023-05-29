/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    const res = [];
    let curr = [];
    for (const val of arr){
        if (curr.length === size){
            res.push(curr);
            curr = [];
        }
        curr.push(val)   
    }
    if (curr.length > 0) res.push(curr);
    return res
};
