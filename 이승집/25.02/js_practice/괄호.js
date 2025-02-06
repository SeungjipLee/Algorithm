const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const T = parseInt(input[0]);
let index = 1;

function isVPS(str) {
    let count = 0;
    for (const ch of str) {
        if (ch === '(') {
            count++;
        } else if (ch === ')') {
            count--;
        }
        if (count < 0) {
            return false;
        }
    }
    return count === 0;
}

for (let i = 0; i < T; i++) {
    const parentheses = input[index++];
    if (isVPS(parentheses)) {
        console.log('YES');
    } else {
        console.log("NO")
    }
}