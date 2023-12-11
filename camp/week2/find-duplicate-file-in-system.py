class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for path in paths:
            path = path.split()
            for file in path[1:]:
                file = file.split("(")
                dic[file[1]].append(path[0]+'/'+file[0])
        ans =[]
        for file in dic:
            if len(dic[file])>1:
                ans.append(dic[file])
        return ans