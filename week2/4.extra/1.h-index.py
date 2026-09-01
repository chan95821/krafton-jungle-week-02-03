from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        sorted_citations = sorted(citations)
        MAX_CITATIONS = 1000 # mutation 제한 안함. naming 관례. 대신 typing에서 Final 도입하면 경고 가능 
        result = 0
        for h in range(n+1 if n < MAX_CITATIONS else MAX_CITATIONS +1):
            least = sorted_citations[-1 * h:] [0] # 만약 범위 넘어가면 slicing은 끝 지점으로 자동 제한
            if least >= h:
                result = h
                continue
            else: 
                break

        return result
        