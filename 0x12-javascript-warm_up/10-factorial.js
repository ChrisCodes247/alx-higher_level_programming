#!/usr/bin/node

const number = parseInt(process.argv[2]);

function factorial(n) {
	if (n < 0) {
		return 1;
	}

	if (n === 0 || n === 1) {
		return 1;
	}else {
	return n * factorial(n - 1);
	}
}

if (isNaN(number) || number < 0) {
	console.log(1);
} else {
	console.log(factorial(number));
}
