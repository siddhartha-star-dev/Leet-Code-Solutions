#best solution 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)-2,-1,-1):
            l=i+1
            while l<len(temperatures):
                if temperatures[l] > temperatures[i]:
                    answer[i]=l-i
                    break
                elif answer[l]==0:
                    break
                else:
                    l+=answer[l]
        return answer

#stack Approach
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = [[temperatures[0],0]]
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT,stackI = stack.pop()
                answer[stackI] = i-stackI
            stack.append([t,i])
        return answer
