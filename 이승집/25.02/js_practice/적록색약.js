const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let inputs = [];

rl.on('line', (line) => {
    inputs.push(line);
    if (inputs.length === parseInt(inputs[0]) + 1) {
        rl.close();
    }
});

rl.on('close', () => {
    let n = parseInt(inputs[0]);
    let board = inputs.slice(1).map((item) => item.split(''));

    let normal = 0;
    let abnormal = 0;
    let visitedNormal = Array.from({ length: n }, () => Array(n).fill(0));
    let visitedAbnormal = Array.from({ length: n }, () => Array(n).fill(0));
    let dx = [0, 1, 0, -1];
    let dy = [1, 0, -1, 0];

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (visitedNormal[i][j] === 1) continue;

            let currentColor = board[i][j];
            let queue = [[i, j]];
            visitedNormal[i][j] = 1;

            while (queue.length) {
                let [x, y] = queue.shift();
                for (let k = 0; k < 4; k++) {
                    let nx = x + dx[k];
                    let ny = y + dy[k];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visitedNormal[nx][ny] && board[nx][ny] === currentColor) {
                        queue.push([nx, ny]);
                        visitedNormal[nx][ny] = 1;
                    }
                }
            }
            normal++;
        }
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (visitedAbnormal[i][j] === 1) continue;

            let currentColor = board[i][j];
            if (currentColor === 'R' || currentColor === 'G') currentColor = 'RG';
            let queue = [[i, j]];
            visitedAbnormal[i][j] = 1;

            while (queue.length) {
                let [x, y] = queue.shift();
                for (let k = 0; k < 4; k++) {
                    let nx = x + dx[k];
                    let ny = y + dy[k];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visitedAbnormal[nx][ny] && currentColor.includes(board[nx][ny])) {
                        queue.push([nx, ny]);
                        visitedAbnormal[nx][ny] = 1;
                    }
                }
            }
            abnormal++;
        }
    }

    console.log(normal, abnormal);
});
