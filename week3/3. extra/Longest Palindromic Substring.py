class Solution:
    def longestPalindrome(self, s: str) -> str:

        #각 위치의 최대 palindrome 개수
   
        max_stat = (1, 0)
        pal_len = [0] * len(s)
        pal_len[0] = 1
        for idx_r, ch_r in enumerate(s):
            if idx_r == 0: continue

            idx_l = idx_r - pal_len[idx_r-1] - 1 # idx_l은 연장 판정할 다음 비교할 대상이 된다.
            ch_l = s[idx_l]
            #palindrome 연장은 항상 한 번 (+2)만큼밖에 안된다. 만약 연장했다면 바로 넘어가면 된다
            if ch_l == ch_r and idx_l >= 0:
                pal_len[idx_r] = pal_len[idx_r-1] + 2
            else:# palindrome 연장 안된다. -> brute force 해봐야? -> 1 또는 2일 것이기 때문에 괜찮아 보인다
                if s[idx_r-1] == s[idx_r]:
                    pal_len[idx_r] = 2
                else: pal_len[idx_r] = 1

            if pal_len[idx_r] > max_stat[0]:
                max_stat = pal_len[idx_r], idx_r
        
        max_len, max_idx_r = max_stat
        return s[max_idx_r-max_len+1: max_idx_r+1]
            
            


                
