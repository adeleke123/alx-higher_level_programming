#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    let result = '';
    while (num > 0) {
      result = (num % base) + result;
      num = Math.floor(num / base);
    }
    return result;
  };
};
