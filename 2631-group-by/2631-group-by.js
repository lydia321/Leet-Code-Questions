/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    //would be easier with defaultdict in python
    const res = {};
    for (const val of this){
        if (fn(val) in res){
            res[fn(val)].push(val);
        }else{
            res[fn(val)] = [val];
        }
        
    }
    return res;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */