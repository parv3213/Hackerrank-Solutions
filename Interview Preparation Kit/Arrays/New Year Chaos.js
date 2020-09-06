"use strict";

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

// Complete the minimumBribes function below.
function minimumBribes(q) {
	var minBribes = 0;
	var expectedFirst = 1;
	var expectedSecond = 2;
	var expectedThird = 3;
	for (var i = 0; i < q.length; i++) {
		if (q[i] === expectedFirst) {
			expectedFirst = expectedSecond;
			expectedSecond = expectedThird;
			expectedThird++;
		} else if (q[i] === expectedSecond) {
			minBribes++;
			expectedSecond = expectedThird;
			expectedThird++;
		} else if (q[i] === expectedThird) {
			minBribes += 2;
			expectedThird++;
		} else {
			return console.log("Too chaotic");
		}
	}
	console.log(minBribes);
}
function main() {
	const t = parseInt(readLine(), 10);

	for (let tItr = 0; tItr < t; tItr++) {
		const n = parseInt(readLine(), 10);

		const q = readLine()
			.split(" ")
			.map((qTemp) => parseInt(qTemp, 10));

		minimumBribes(q);
	}
}
