class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # print(colors[:-1])
        count1, count2 = 0, 0
        for i in range(1, len(colors)-1):

            if colors[i-1] == colors[i] == colors[i+1] == "A":
                count1 += 1

            elif colors[i-1] == colors[i] == colors[i+1] == "B":
                count2 += 1

        return count1 > count2
