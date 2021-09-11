class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ht = defaultdict(list)
        for word in words:
            c = word[0]
            ht[c].append(iter(word[1:]))
            
        count = 0
        for c in s:
            copy = ht[c]
            ht[c] = []
            for it in copy:
                nextC = next(it, None)
                if not nextC:
                    count += 1
                else:
                    ht[nextC].append(it)
        return count
        
        
'''
brute force:
for word in words:
    two pointer -> O(s + w)
    
move through s only once -> O(s)

abcde
[a]
{"a": a->(final, "a"), b: b->b->(final, bb), a: a->c->d->(final, acd), a: a-c-e-(final, ace)}

special node that keeps track of characters

instead of using linkedlists, it's much better to use iterators!!!

python iterators!!!
O(s + w*c)
'''
