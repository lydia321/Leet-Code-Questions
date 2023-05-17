/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const res = [];
    for (let i in arr) { // in - will give you the index
                        // of will give you the value
        if(fn(arr[i], Number(i))) {
            res.push(arr[i])
        }
    }
    return res
};