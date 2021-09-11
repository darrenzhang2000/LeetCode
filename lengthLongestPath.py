class Solution:
    def lengthLongestPath(self, input):
        maxlen = 0
        depth = {0:0}
        for line in input.split('\n'):
            name = line.lstrip('\t')
            level = (len(line) - len(name)) + 1
            print(level)
            if '.' in name:
                maxlen = max(maxlen, depth[level - 1] + len(line))
            else:
                depth[level] = depth[level - 1] + len(name)
        return maxlen
