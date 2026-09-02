class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 300 * 299 개 선택  * 나머지 298개 비교 
        #  300 * 299 개에 대해 max 집합 탐색
        max = -1
        if len(points) == 1:
            return 1
#  -> 직선 저장하려면 정규화해야한다 - gcd로 나누기, 부호 고려 / set으로 만들어서 dictionary 완성 이후 전체 점 비교하면 N^2 으로 가능/// 
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                count = 0
                x1, y1 = points[i]
                x2, y2 = points[j]
                #  i.x a + i.y + b
                # y = (y1 - y2) / (x1 - x2) x + y1 - ((y1 - y2) / (x1 - x2)) * x1
                if x1 == x2:
                    checker = lambda x, y : True if x == x1 else False
                else:
                    # checker = lambda x, y : True if ( y == (( (y1 - y2) / (x1 - x2)) * x + y1 - ((y1 - y2) / (x1 - x2)) * x1 ) ) else False
                    checker = lambda x, y : True if ( y * (x1 - x2) == (y1 - y2) * x + y1 * ( x1 - x2) - (y1 - y2) * x1) else False
                for cand in points:
                    if checker(cand[0], cand[1]):
                        count += 1

                if max< count:
                    max = count

        return max

        