/**
 * @param {object} obj1
 * @param {object} obj2
 * @return {object}
 */
function objDiff(o1, o2) {
    //only care about common keys
    /*
    Get diff if:
    1) if one is an obj and other isnt (if they are different types)
    2) if both are primitive and different
    
    ELSE:
    if they are both objs or arrs: Recursion
    
    */
    //Are both objs primitives?
    if (!isObject(o1) && (!isObject(o2))){
        return o1 === o2 ? {} : [o1, o2];
    }
    
    //Is just one primitive
    if (!isObject(o1) || (!isObject(o2))){
        return  [o1, o2];
    }
    //Is one just an arr?
    if (Array.isArray(o1) !== Array.isArray(o2)){
        return  [o1, o2];
    }
    const diff = {};
    //if both are arrs or objs
    //We only have to check through one of the objs because we only want common keys
    for (const key in o1){
        if (key in o2){
            const res = objDiff(o1[key],o2[key]);
            if (Object.keys(res).length > 0){
                diff[key] = res;
            }
        }
    }
    
    return diff;
    
    function  isObject(obj){
        return typeof obj === 'object' && obj !== null;
    }
};