// Array.from()
// let str = 'naseem'
// console.log(Array.from(str));

// let numbers = [1, 2, 3, 4];
// console.log(Array.from(numbers, num => num + num));

// array from set
// console.log(Array.from(new Set(['this', 'is', 'is', 'set'])));
// console.log(Array.from(new Set(['this', 'is', 'is', 'set']), s => s + s));
// console.log(Array.from(new Set(['this', 'is', 'is', 'set']), (s, i) => s + i));

// array from map
// console.log(Array.from(new Map([['key1', 'value1'], ['key2', 'value2']])));
// console.log(Array.from(new Map([['key1', 'value1'], ['key2', 'value2']]).keys()));
// console.log(Array.from(new Map([['key1', 'value1'], ['key2', 'value2']]).values()));

// Array from an Array-like object (arguments)
// function f() {
//      return Array.from(arguments)
// }
// f('nasee')

// console.log(Array.from({ length: 2.5 }, (v, i) => (v, i)));
// Sequence generator function (commonly referred to as "range", e.g. Clojure, PHP etc)
const range = (start, stop, step = 1) => Array.from({ length: (stop - start) / step + 1 }, (_, i) => start + (i * step));
console.log(range(0, 5, 3));