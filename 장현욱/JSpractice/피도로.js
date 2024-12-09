function solution(k, dungeons) {
  var answer = -1;
  const dungeon = []
  const n = dungeons.length
  const stack = [[[], Array.from(dungeons)]]

  while (stack.length > 0) {
    const [current, remaining] = stack.pop()

    if(current.length === n) {
      dungeon.push(current) // 순열 완성
    } else {
      for (let i = 0; i < remaining.length; i++) {
        const next = remaining.slice()
        const removed = next.splice(i, 1)
        stack.push([current.concat(removed), next])
      }
    }
  }

  for (const nowPlan of dungeon) {
    let nowK = k
    let nowComplete = 0
    for (const now of nowPlan) {
      if (nowK >= now[0]) {
        nowComplete += 1
        nowK -= now[1]
      } else {
        break
      }
    }
    answer = Math.max(nowComplete, answer)
    nowComplete = 0
    if (answer === dungeons.length) {
      break
    }
  }

  return answer;
}

function permutations(arr) {
  const results = [];
  const n = arr.length;
  const stack = [[[], Array.from(arr)]]; // [현재 순열, 남은 숫자]

  while (stack.length > 0) {
      const [current, remaining] = stack.pop();

      if (current.length === n) {
          results.push(current); // 순열 완성
      } else {
          for (let i = 0; i < remaining.length; i++) {
              const next = remaining.slice(); // 남은 숫자 복사
              const removed = next.splice(i, 1); // i번째 숫자 제거
              stack.push([current.concat(removed), next]); // 스택에 추가
          }
      }
  }

  return results;
}

// 테스트
console.log(permutations([1, 2, 3]));