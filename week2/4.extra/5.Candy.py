class Solution:
    def candy(self, ratings: List[int]) -> int:
        visited = [False for _ in ratings]
        count = [0 for _ in ratings]
        def find(idx):
            if visited[idx]:
                return count[idx]
            else:
                current_count = 1
                l, r = idx -1, idx + 1
                if l >= 0:
                    l_rating = ratings[l]
                    if l_rating < ratings[idx]:
                        current_count = max(current_count, find(l) + 1)
                if r < len(ratings):
                    r_rating = ratings[r]
                    if r_rating < ratings[idx]:
                        current_count = max(current_count, find(r) + 1)
                
                count[idx] = current_count
                visited[idx] = True
                return current_count

        for i in range(len(ratings)):
            find(i)
        return sum(count)

