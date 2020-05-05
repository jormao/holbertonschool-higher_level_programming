#!/usr/bin/node
const myObject = {
  type: 'object',
  alue: 12
};
console.log(myObject);
myObject.incr = function () {
  myObject.value += 1;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
