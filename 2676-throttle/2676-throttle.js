/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
/**
Eg. Leetcode RunCode
Concept Prevent a code from being called more frequently than it can handle.
Recursion concept: recursivly call nextargs when its time, if any

1) if its not ready to excecute it should override any nextargs if any
2)else excecute and set timer for when your ready to exceute again. if you have waiting args 

*/
var throttle = function(fn, t) {
    let readytoexecute = null;
    let nextargs = null;
    
    const nextfn = () => { // will excecute next args, if any
        if (nextargs == null){
            readytoexecute = null;
        }else{
            fn(...nextargs);
            nextargs = null;
            readytoexecute = setTimeout(nextfn,t);
        }       
    };
    
  return function(...args) {
      if (readytoexecute){
          nextargs = args; //override any waiting next args
          
      }else{
          fn(...args);
          // its gonna start executing after certain  amount of time, if it has next args
          readytoexecute = setTimeout(nextfn,t); 
      }
  }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */