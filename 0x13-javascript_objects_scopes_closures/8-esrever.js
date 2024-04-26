#!/usr/bin/node

exports.esrever = function (list) {
    return list.map((element, index) => list[list.length - 1 - index]);
}
