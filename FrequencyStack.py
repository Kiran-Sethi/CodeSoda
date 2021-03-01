'''
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3655/
'''

class FreqStack:

    def __init__(self):
        self.frequencyStack = []
        self.frequencies = {}

    def push(self, x: int) -> None:
        self.frequencyStack.append(x)
        if x in self.frequencies:
            self.frequencies[x] += 1
        else:
            self.frequencies[x] = 1

    def pop(self) -> int:
        top = len(self.frequencyStack) - 1
        maxm_freq=0
        for keys in self.frequencies:
                if maxm_freq<self.frequencies[keys]:
                    maxm_freq=self.frequencies[keys]
        while top>=0:
            key=self.frequencyStack[top]
            if self.frequencies[key]==maxm_freq:
                self.frequencies[key] -= 1
                return self.frequencyStack.pop(top)
            top=top-1

'''
my result  complexity - O(N)-space
time complexity - O(N)for push  ,O(N) for pop

'''
'''best time complexity -- 
O(1)  for both push and pop
'''
'''best space complexity
O(N)
'''
