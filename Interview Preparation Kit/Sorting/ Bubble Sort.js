"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
	inputString += inputStdin;
});

process.stdin.on("end", function () {
	inputString = inputString
		.replace(/\s*$/, "")
		.split("\n")
		.map((str) => str.replace(/\s*$/, ""));

	main();
});

function readLine() {
	return inputString[currentLine++];
}

// Complete the countSwaps function below.
function countSwaps(a) {
	var _a;
	var swapCount = 0;
	var isSorted = false;
	for (var i = 0; i < a.length; i++) {
		isSorted = true;
		for (var j = 1; j < a.length - i; j++) {
			if (a[j - 1] > a[j]) {
				swapCount++;
				(_a = swap(a[j - 1], a[j])), (a[j - 1] = _a[0]), (a[j] = _a[1]);
				isSorted = false;
			}
		}
		if (isSorted === true) {
			break;
		}
	}
	console.log("Array is sorted in " + swapCount + " swaps.");
	console.log("First Element: " + a[0]);
	console.log("Last Element: " + a[a.length - 1]);
}
function swap(a, b) {
	var temp = a;
	a = b;
	b = temp;
	return [a, b];
}

function main() {
	const n = parseInt(readLine(), 10);

	const a = readLine()
		.split(" ")
		.map((aTemp) => parseInt(aTemp, 10));

	countSwaps(a);
}
