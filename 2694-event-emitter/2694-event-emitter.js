class EventEmitter {
    eventMap = {};
  subscribe(event, cb) {
      if (!(event in this.eventMap)){ 
          this.eventMap[event] = new Set();
          
      }
      this.eventMap[event].add(cb);
      
    return {
        unsubscribe: () => {
            this.eventMap[event].delete(cb);
        
        },
    };
  }

  emit(event, args = []) {
      const res = [];
      if (!(event in this.eventMap)) return [];
      for (const fn of this.eventMap[event]){
          res.push(fn(...args))
      }
      return res;

  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */