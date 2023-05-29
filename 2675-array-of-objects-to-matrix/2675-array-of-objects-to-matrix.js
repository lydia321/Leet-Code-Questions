/**
 * @param {Array} arr
 * @return {Matrix}
 */
var jsonToMatrix = function(arr) {
    const keySet = new Set();
    for (const obj of arr){
        getKeys(obj,'')
    }
    const keys = Array.from(keySet).sort();
    const res = [keys]
    
    for (const obj of arr){
        const keytoVal = {};
        getValues (obj,'',keytoVal);
        let row = []
        for (const key of keys){
            if(key in keytoVal){
                row.push(keytoVal[key]);
            }else{
                row.push('');
            }
        } 
        res.push(row);
    }
    return res
    
    function getKeys(obj,path) {
        for (const key in obj){
            const newpath = path ? `${path}.${key}` : key ;
            if(isObject(obj[key])){//is the key is another object?
                getKeys(obj[key] ,newpath)
            }else{
                keySet.add(newpath);
            }
        }
    }
    
    function getValues(obj,path,keytoVal){
        for (const key in obj){
            const newpath = path ? `${path}.${key}` : key ;
            if (isObject(obj[key])){
                getValues(obj[key],newpath,keytoVal)
            }else{
                //base Case
                keytoVal[newpath] = obj[key];
            }
        }
        
    }
    
    function isObject(obj){//check if its an object
        return obj !== null && typeof obj === 'object';
    }
    
};