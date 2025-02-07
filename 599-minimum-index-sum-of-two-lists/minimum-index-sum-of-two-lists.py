class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        common = defaultdict(list)
        ans = []
        for i in range(len((list1))):
            for j in range(len(list2)):

                if list1[i] == list2[j]:
                    common[list1[i]] = i+j

        min_value = min(common.values())
        
        for key in common:
            if common[key] == min_value:
                ans.append(key)

        return ans        























        # min_index_sum = -1
        # ans_dict = {}
        # ans = []
        # for i in range(len(list1)):
        #     for j in range(len(list2)):
        #         if list1[i] == list2[j]:
        #             # min_index_sum = min(min_index_sum, i+j)
        #             # ans = [list1[i]]
        #             ans_dict[i+j] = list1[i]
        # sorted_dict = dict(sorted(ans_dict.items(), key=lambda x : x))
        # min_index_sum = min(sorted_dict.values())

        # # for val,min_index_sum in sorted_dict:
        #     ans.append([val])
        # return ans        









        