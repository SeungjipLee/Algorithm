function findLongestPathLength(N, relation, dirname) {
  // 트리 구조를 위한 인접 리스트 생성
  let tree = Array.from({ length: N + 1 }, () => []);
  
  // 부모-자식 관계를 기반으로 트리 생성
  relation.forEach(([parent, child]) => {
      tree[parent].push(child);
  });
  
  // DFS를 사용하여 가장 긴 경로 길이 계산
  function dfs(node) {
      if (tree[node].length === 0) {
          return dirname[node - 1].length; // 리프 노드의 경우 자기 이름의 길이 반환
      }
      
      let maxLength = 0;
      
      for (const child of tree[node]) {
          maxLength = Math.max(maxLength, dfs(child));
      }
      
      return dirname[node - 1].length + maxLength + 1; // 자기 이름의 길이 + 최대 하위 경로 길이 + 슬래시
  }
  
  return dfs(1) - 1; // 루트 노드(디렉토리 1)에서 시작하므로 슬래시 제거
}
