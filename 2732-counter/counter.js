/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let count = n;

    function counter() {
        const current = count;
        count++;
        return current;
    }

    return counter; // Return the inner counter function
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */