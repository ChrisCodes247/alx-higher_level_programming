#!/usr/bin/node

exports.esrever = function (list) {
	let count = list.length;
	let newlist = [];
	 for (let i = 0; i < list.length; i++) {
		      count -= 1;
		      newlist.push(list[count]);
		  }
	return newlist;
}
