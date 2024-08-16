#!/usr/bin/node

let n = process.argv[2];
const lst = ["C is fun"];

if (isNaN(n)) {
	  console.log("Missing number of occurrences");
} else {
	  for (i = 0; i < n; i++) {
		    console.log(lst);
	  }
}
