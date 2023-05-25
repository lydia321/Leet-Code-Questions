/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    //Base Case, you can directly convert to string
    if (object === null || object === undefined){
        return String(object);
    }
    //Array
    if (Array.isArray(object)){
        const res = object.map((obj) => jsonStringify(obj));
        return `[${res.join(',')}]`;
    }
    //Object
    if (typeof object === 'object'){
        const keys = Object.keys(object);//get all keys to a constant variable obj
        const res = keys.map((key) => `"${key}":${jsonStringify(object[key])}`);
        return `{${res.join(',')}}`
                 
    }
    if (typeof object === 'string'){
        return `"${String(object)}"`
    }
    
    
    
    return String(object); // for booleans and numbers;
};