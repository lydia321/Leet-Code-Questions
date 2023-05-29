/**
 * @param {Object} object
 * @param {Function} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj === null || obj === undefined || typeof classFunction !== 'function'){
        return false;
    }
    let currp = Object.getPrototypeOf(obj);
    // We do this lil prototype runaround because prototypes are hidden in objects(we cant acces them using .prototype fn). But classes have access to their prototypes.
    while (currp !== null){
        if (currp === classFunction.prototype){//basecase
            return true;
        }
        currp = Object.getPrototypeOf(currp);
        
    }
    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */