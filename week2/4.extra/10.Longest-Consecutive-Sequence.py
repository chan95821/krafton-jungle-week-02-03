class Amoeba:
    def __init__(self, num):
        self.len = 1
        self.max = num
        self.min = num

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 숫자가 등장했다면, 어떤 amoeba든 가리켜야 한다 
        # 가리키는 basket에 대해, 중간 번호들은 합치려는 것들과 상호작용 안하므로, 양 끝만 최신이면 된다.
        nums_dict = {}  # amoeba (basket) 가리킨다. 
        largest = 0
        for num in nums:
            u, d = num + 1, num - 1
            if nums_dict.get(num) is not None:
                continue
            # -> 최적화 위해 객체를 미리 구해놓기?
            if nums_dict.get(u) is not None and nums_dict.get(d) is not None: # 양 옆이 존재. amoeba 중 하나를 선택하고, max, min, len 업데이트 
                new_amoeba = nums_dict[u]
                new_amoeba.max = nums_dict[u].max
                new_amoeba.min = nums_dict[d].min
                new_amoeba.len = nums_dict[u].len + nums_dict[d].len + 1
                nums_dict[new_amoeba.max] = new_amoeba
                nums_dict[new_amoeba.min] = new_amoeba
                nums_dict[num] = new_amoeba
                largest = max(largest, new_amoeba.len)
            elif nums_dict.get(d) is not None:
                nums_dict[num] = nums_dict[d]
                nums_dict[d].max = num
                nums_dict[d].len += 1
                largest = max(largest, nums_dict[d].len)
            elif nums_dict.get(u) is not None:
                nums_dict[num] = nums_dict[u]
                nums_dict[u].min = num
                nums_dict[u].len += 1
                largest = max(largest, nums_dict[u].len)
            elif nums_dict.get(d) is None and nums_dict.get(u) is None:
                nums_dict[num] = Amoeba(num)
                largest = max(largest, nums_dict[num].len)
        return largest


            