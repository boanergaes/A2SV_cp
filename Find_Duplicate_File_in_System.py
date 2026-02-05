#leetcode 

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        buff = {}

        for path in paths:
            iparr = path.split(' ')
            directory = iparr[0]
            for i in range(1, len(iparr)):
                content = []
                flag = False
                filename = []
                for c in iparr[i]:
                    if c == '(':
                        flag = True
                    if c == ')':
                        flag = False
                        break
                    if flag:
                        content.append(c)
                    else:
                        filename.append(c)

                content = ''.join(content)
                filename = ''.join(filename)

                to_add = buff.get(content, [])
                to_add.append(directory + '/' + filename)


                buff [content] = to_add

        
        return [buff[k] for k in buff if len(buff[k]) > 1]
        
