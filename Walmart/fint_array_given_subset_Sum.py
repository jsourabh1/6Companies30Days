class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums = sorted(sums, reverse=True)
        ans = []

        def remove(sumset, ele):
            if sumset[ele] > 1:
                sumset[ele] -= 1
            else:
                del sumset[ele]

        while len(sums) > 2:
            array1, array2 = [], []
            num = sums[0] - sums[1]
            sumset = Counter(sums)
            for ele in sums:
                if ele in sumset:
                    array2.append(ele)
                    array1.append(ele - num)
                    remove(sumset, ele)
                    remove(sumset, ele - num)
            if num in array2:
                idx = array2.index(num)
                if array1[idx] == 0:
                    ans.append(num)
                    sums = array1
                    continue
            ans.append(-1 * num)
            sums = array2

        return ans + [sums[1]] if sums[0] == 0 else ans + [sums[0]]