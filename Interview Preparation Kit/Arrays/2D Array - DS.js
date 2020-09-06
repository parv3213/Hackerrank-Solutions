"use strict";

const fs = require("fs");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
	inputString += inputStdin;
});

process.stdin.on("end", (_) => {
	inputString = inputString
		.replace(/\s*$/, "")
		.split("\n")
		.map((str) => str.replace(/\s*$/, ""));

	main();
});

function readLine() {
	return inputString[currentLine++];
}

// Complete the hourglassSum function below.
function hourglassSum(arr) {
	var sumArr = [];
	for (var rowNo = 0; rowNo <= 3; rowNo++) {
		for (var colNo = 0; colNo <= 3; colNo++) {
			var sum = 0;
			for (var row = 0 + rowNo; row <= 2 + rowNo; row++) {
				for (var col = 0 + colNo; col <= 2 + colNo; col++) {
					if (!((row === 1 + rowNo && col === 0 + colNo) || (row === 1 + rowNo && col === 2 + colNo))) {
						sum += arr[row][col];
					}
				}
			}
			sumArr.push(sum);
		}
	}
	return Math.max.apply(Math, sumArr);
}

function main() {
	const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

	let arr = Array(6);

	for (let i = 0; i < 6; i++) {
		arr[i] = readLine()
			.split(" ")
			.map((arrTemp) => parseInt(arrTemp, 10));
	}

	let result = hourglassSum(arr);

	ws.write(result + "\n");

	ws.end();
}
