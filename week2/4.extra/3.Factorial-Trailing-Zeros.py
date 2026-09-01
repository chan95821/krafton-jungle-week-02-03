class Solution:
    def trailingZeroes(self, n: int) -> int:
        #  10은 5 *2. (5 * 2) ^ n 이 되는 n 개수 찾기
        if n == 0: return 0
        fives = 0
        twos = 0
        for i in range(1, n + 1):
            while i % 5 == 0: # input constraint에 의해 최대 4번
                fives += 1
                i //= 5 # /= 5를 하면, i가 float 될 수 있다. 그러면 while문 조건 만족 안될 수 있음
            while i % 2 == 0: # 동일하게 최대 4번 
                twos += 1
                i //= 2
        
        return fives if fives < twos else twos