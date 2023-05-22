/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
/**
Question breakdown: basically when a fn is excecuting after some t delay, if same fn is called before the previous one has excecuted, clear previous request and continue with the new request.
If Fn has already executed, just continue with next request.

Concept: - You set the time out to be delayed by the given t, to perform fn(...args).
         - clearTimeout function will clear fn's that have not been excecuted when another fn is called
         - If an Fn is excecuted before another fn is called, clearTimout wont affect anything
*/
var debounce = function(fn, t) {
    let id;
    return function(...args) {
        clearTimeout(id); 
        id = setTimeout(() => {
            fn(...args)
        },t);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */