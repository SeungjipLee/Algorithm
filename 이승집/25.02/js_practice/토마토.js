const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let inputs = [];

rl.on('line', (line) => {
    inputs.push(line.split(' ').map(Number));
    if (inputs.length === inputs[0][1] + 1) {
        rl.close();
    }
});

rl.on('close', () => {
    let n = inputs[0][1];
    let m = inputs[0][0];
    let boards = inputs.slice(1);

    let dx = [0, 1, 0, -1];
    let dy = [1, 0, -1, 0];

    let ready = 0;
    let tomatoes = [];

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (boards[i][j] === 0) {
                ready += 1;
            } else if (boards[i][j] === 1) {
                tomatoes.push([i, j, 0]);
            }
        }
    }

    if (ready === 0) {
        console.log(0);
        process.exit();
    }

    let ans = 0;
    let front = 0;
    
    while (front < tomatoes.length) {
        let [nowX, nowY, turn] = tomatoes[front++];
        ans = Math.max(ans, turn);

        for (let k = 0; k < 4; k++) {
            let newX = nowX + dx[k];
            let newY = nowY + dy[k];

            if (0 <= newX && newX < n && 0 <= newY && newY < m && boards[newX][newY] === 0) {
                boards[newX][newY] = 1;
                tomatoes.push([newX, newY, turn + 1]);
                ready -= 1;
            }
        }
    }

    console.log(ready !== 0 ? -1 : ans);
});
