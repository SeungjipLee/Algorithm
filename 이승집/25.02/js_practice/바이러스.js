const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', (line) => {
    input.push(line.trim());

    if (input.length === parseInt(input[1]) + 2) {
        rl.close();
    }
});

rl.on('close', () => {
    let n = parseInt(input[0]);
    let infos = input.slice(2).map(line => line.split(' ').map(Number));
    let adj = Array.from({ length: (n+1) }, () => []);
    for (const ch of infos) {
        const [a, b] = ch;
        adj[a].push(b);
        adj[b].push(a);
    }
    let visited = Array(n+1).fill(0);
    let Q = [1];
    let answer = -1;
    visited[1] = 1;
    while (Q.length >= 1) {
        now = Q.shift();
        answer += 1;
        for (let nxt of adj[now]) {
            if (visited[nxt] == 0) {
                Q.push(nxt);
                visited[nxt] = 1;
            }
        }
    }

    console.log(answer);
});
