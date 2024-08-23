function solution(n, v) {
  if (n <= 1) return 0; // 최소 2일 이상 필요

  let maxProfit = 0; // 최대 이익 초기화
  let minPriceAfter = new Array(n).fill(0);
  
  // 각 날짜 이후의 최소 가격을 저장
  minPriceAfter[n - 1] = v[n - 1];
  for (let i = n - 2; i >= 0; i--) {
      minPriceAfter[i] = Math.min(minPriceAfter[i + 1], v[i]);
  }
  
  // 최대 이익을 계산
  for (let i = 0; i < n - 1; i++) {
      let profit = v[i] - minPriceAfter[i + 1];
      maxProfit = Math.max(maxProfit, profit);
  }

  return maxProfit;
}
