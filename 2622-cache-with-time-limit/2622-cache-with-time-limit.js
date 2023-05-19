
var TimeLimitedCache = function() {
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    // if key already exists, we have to override the timeout
    const Exist = this.cache.get(key);
    if (Exist) {
        clearTimeout(Exist.timeoutId);
    }
    const timeoutId = setTimeout(() => this.cache.delete(key),duration);
    this.cache.set(key, {value,timeoutId });
    return Boolean(Exist);
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (this.cache.has(key)) {
        return this.cache.get(key).value;
    } else {
        return -1
    }
}    

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
   return this.cache.size;
}

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */