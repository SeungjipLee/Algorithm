const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n = 0;
let ans = [];
let cnt = 0;

rl.on('line', (line) => {
    if (n === 0) {
        n = parseInt(line);
    } else {
        ans.push(line);
        cnt++;
    }
    if (cnt === n) {
        rl.close();
    }
})

rl.on('close', () => {
    for (let i = 0; i < n; i++) {
        const [a, b] = ans[i].split(' ').map(Number);
        console.log(`Case #${i+1}: ${a+b}`);
    }
    process.exit();
})