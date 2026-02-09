class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        line_buff = []
        block_flag = False

        for i in range(len(source)):
            curr_line = source[i]
            l = len(curr_line)

            j = 0
            while j < l:
                if j < l-1 and curr_line[j:j+2] == '/*' and not block_flag:
                    j += 2
                    block_flag = True
                    continue

                elif block_flag and j < l-1 and curr_line[j:j+2] == '*/':
                    block_flag = False
                    j += 2
                    continue

                elif not block_flag and j < l-1 and curr_line[j:j+2] == '//':
                    break
                 
                elif not block_flag and j < l:  
                    line_buff.append(curr_line[j])
                    j += 1

                else:
                    j += 1
                
            if not block_flag and line_buff:
                res.append(''.join(line_buff))
                line_buff.clear()

        return res