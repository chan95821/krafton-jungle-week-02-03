class Solution:
    def longestPalindrome(self, s: str) -> str:

        #각 위치의 최대 palindrome 개수
   
        max_stat = (1, 0)
        pal_len = [0] * len(s)
        pal_len[0] = 1
        for idx_r, ch_r in enumerate(s):
            if idx_r == 0: continue

            idx_l = idx_r - pal_len[idx_r-1] - 1 # idx_l은 연장 판정할 다음 비교할 대상이 된다.
            
            #palindrome 연장은 항상 한 번 (+2)만큼밖에 안된다. 만약 연장했다면 바로 넘어가면 된다
            ch_l = s[idx_l]
            if ch_l == ch_r and idx_l >= 0: # -1 되는 경우  걸러야
                pal_len[idx_r] = pal_len[idx_r-1] + 2
            else:# palindrome 연장 안된다. -> brute force 해봐야?
                for new_l in range(0, idx_r+1): O(N)
                    if s[new_l:idx_r+1] == s[new_l:idx_r+1][::-1]: # O(N)
                        pal_len[idx_r] = idx_r - new_l + 1
                        break      # 합해서 O(N^2) 이고, 전체 순회 까지 포함하면 O(N^3) ... 부적절

            if pal_len[idx_r] > max_stat[0]:
                max_stat = pal_len[idx_r], idx_r
        
        max_len, max_idx_r = max_stat
        return s[max_idx_r-max_len+1: max_idx_r+1]
            
            


                