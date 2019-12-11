from collections import deque
from bisect import insort

class RuleMap:
    def __init__(self,n):
        self._n = n
        self._rules = {}

    def add_rule(self, rule, value):
        rules = self._rules
        for i,x in enumerate(rule):
            if x not in rules:
                rules[x] = {}
            if i == self._n-1:
                rules[x] = value
            else:
                rules = rules[x]

    def get_value(self,rule):
        ans = []
        q = deque()
        
        #rule/similarity/index
        q.append([self._rules,0,0])

        while q:
            curr_rule,similarity,idx = q.popleft()
            if rule[idx] in curr_rule:
                if idx==self._n-1:
                    insort(ans,(similarity+1,curr_rule[rule[idx]]))
                else:
                    q.append([curr_rule[rule[idx]],similarity+1,idx+1])
            
            if '*' in curr_rule:
                if idx==self._n-1:
                    insort(ans,(similarity,curr_rule['*']))
                else:
                    q.append([curr_rule['*'],similarity,idx+1])
        
        return ans and ans[-1][1]

if __name__ == '__main__':
    data =  [
                [3,
                    [
                        [['A1','B1','C1'],30],
                        [['*','B1','C2'],20],
                        [['A2','B1','*'],25]
                    ],
                    [
                        [['A1','B1','C1'],30],
                        [['A1','B1','C2'],20],
                        [['A2','B1','C3'],25]
                    ]
                ]
            ]
    
    print("Check rules with maximum match: ")
    for d in data:
        rm = RuleMap(d[0])
        for r in d[1]:
            rm.add_rule(*r)

        for r in d[2]:
            print('for rule: ', r[0], 'output is', rm.get_value(r[0]), 'expected', r[1])



    