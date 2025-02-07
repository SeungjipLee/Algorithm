function cntSystem(k) {
    let val = '';
    while (k >= 5) {
        k -= 5;
        val += '++++ ';
    }
    if (k > 0) {
        val += '|'.repeat(k);
    }
    return val;
}

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let inputLines = [];
let numberOfInputs = 0;

rl.on('line', (line) => {
    inputLines.push(line);
    if (inputLines.length === parseInt(inputLines[0]) + 1) {
        rl.close();
    }
});

rl.on('close', () => {
    numberOfInputs = parseInt(inputLines[0]);
    for (let i = 1; i <= numberOfInputs; i++) {
        let m = parseInt(inputLines[i]);
        console.log(cntSystem(m));
    }
});
