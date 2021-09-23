class Solution:
    def originalDigits(self, s: 'str') -> 'str':
        # building hashmap letter -> its frequency
        count = collections.Counter(s)
        
        # building hashmap digit -> its frequency 
        out = {}
        # letter "z" is present only in "zero"
        out["0"] = count["z"]
        # letter "w" is present only in "two"
        out["2"] = count["w"]
        # letter "u" is present only in "four"
        out["4"] = count["u"]
        # letter "x" is present only in "six"
        out["6"] = count["x"]
        # letter "g" is present only in "eight"
        out["8"] = count["g"]
        # letter "h" is present only in "three" and "eight"
        out["3"] = count["h"] - out["8"]
        # letter "f" is present only in "five" and "four"
        out["5"] = count["f"] - out["4"]
        # letter "s" is present only in "seven" and "six"
        out["7"] = count["s"] - out["6"]
        # letter "i" is present in "nine", "five", "six", and "eight"
        out["9"] = count["i"] - out["5"] - out["6"] - out["8"]
        # letter "n" is present in "one", "nine", and "seven"
        out["1"] = count["n"] - out["7"] - 2 * out["9"]

        # building output string
        output = [key * out[key] for key in sorted(out.keys())]
        return "".join(output)

# class Solution:
#     def originalDigits(self, s: str) -> str:
#         def foundInAndRemove(ht, numString):
#             charCounts = Counter(numString)
#             hasAllChars = all(ht[k] >= v for k, v in charCounts.items())
#             if hasAllChars:
#                 for k, v in charCounts.items():
#                     ht[k] -= v
#             return len(numString) if hasAllChars else 0
                
                
            
#         chars = ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]
#         ht = {c: 0 for c in chars}
#         for c in s:
#             ht[c] += 1
#         res = []
#         remainingChars = len(s)
#         while remainingChars > 0:
#             words = ['zero', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'one']
#             i = 0
#             while remainingChars and i < len(words):
#                 print(i, remainingChars, ht)
#                 found = foundInAndRemove(ht, words[i])
#                 remainingChars -= found
#                 if found:
#                     res.append(words[i])
#                 else:
#                     i += 1
#                 if remainingChars == 0:
#                     break
#         m = {'zero': 0, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'one':1}
#         return "".join(sorted(list(map(lambda c: str(m[c]), res))))
                
                
            
# #         zero - z
# #         two -> w
# #         three -> h
# #         four -> u
# #         five -> v
# #         six -> x
# #         seven -> v
# #         eight -> g
        
# #         nine -> i after all the above has been found
# #         one -> o after all the above has been found
