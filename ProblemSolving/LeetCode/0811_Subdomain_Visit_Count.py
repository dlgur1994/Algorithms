from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dom_dict = {}
        for e in cpdomains:
            cnt, subdomain = e.split(' ')
            sub = subdomain.split('.')
            for i in range(len(sub)):
                domain = '.'.join(sub[i:len(sub)])
                if domain in dom_dict:
                    dom_dict[domain] += int(cnt)
                else: dom_dict[domain] = int(cnt)
        output_list = []
        for subdom, cnt in dom_dict.items():
            output_list += [str(cnt)+ ' '+ subdom]
        return output_list


input_list = list(map(str,read().rstrip().lstrip('["').rstrip('"]').split('\", \"')))
mod = Solution()
print(mod.subdomainVisits(input_list))
