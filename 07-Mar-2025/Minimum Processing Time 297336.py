# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)

        max_time = 0
        task_index = 0

        for i in range(len(processorTime)):
            end_time = max(processorTime[i] + tasks[task_index + j] for j in range(4))
            max_time = max(max_time, end_time)

            task_index+=4

        return max_time
