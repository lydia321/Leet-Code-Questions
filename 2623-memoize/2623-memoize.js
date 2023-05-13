/**
 * @param {Function} fn
 */
function memoize(fn) {
    const cache = {};
    return function(...args) {
        const inpt = JSON.stringify(args)
        if (inpt in cache) {
            return cache[inpt];
        } 
        const functionOutput = fn(...args);
        cache[inpt] = functionOutput;
        return functionOutput;
            
        }
        
    }



/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */