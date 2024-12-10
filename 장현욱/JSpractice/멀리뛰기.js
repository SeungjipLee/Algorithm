function solution(n) {
  // 동적계획법을 이용한 피보나치
  const dp = Array.from({length:n}).fill(0); // n길이의 dp배열을 생성
  dp[0] = 1, dp[1] = 1; // 0번과 1번에 1 대입
  
  // 피보나치 풀이, 다만 dp배열에 넣을 때, %1234567을 해줘야 에러가 나지 않는다.
  for (let i=2; i<=n; i++) {
      dp[i] = (dp[i-2] + dp[i-1])%1234567;
  }
  
  return dp[n];
}