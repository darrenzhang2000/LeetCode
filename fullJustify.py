class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        left, right = 0, 0
        res = []
        while right < len(words):
            right, line_min_char_count = self.find_right(left, words, maxWidth)
            line = self.justify(left, right, line_min_char_count, words, maxWidth)
            res.append(line[:])
            left, right = right + 1, right + 1
        return res
    
    def find_right(self, left, words, maxWidth):
        line_min_char_count = len(words[left])
        right = left
        is_extra_word_counted = True
        while line_min_char_count <= maxWidth:
            if right+1 >= len(words):
                is_extra_word_counted = False
                break
            line_min_char_count += len(words[right+1])+1
            right += 1
            
        if is_extra_word_counted:
            right -= 1
            line_min_char_count -= (len(words[right+1])+1)
        return right, line_min_char_count
    
    def justify(self, left, right, line_min_char_count, words, maxWidth):
        is_last_line = right == len(words)-1
        line_num_words = right - left + 1
        if is_last_line:
            return self.justify_last_line(left, line_min_char_count, words, maxWidth)
        elif (line_num_words > 1):
            return self.justify_non_last_line(left, right, line_min_char_count, words, maxWidth)
        elif (line_num_words == 1):
            return self.justify_single_word_line(left, line_min_char_count, words, maxWidth)
        
    def justify_non_last_line(self, left, right, line_min_char_count, words, maxWidth):
        total_extra_spaces = maxWidth-line_min_char_count
        line_num_words = right-left+1
        if line_num_words > 1:
            min_spaces = 1 + total_extra_spaces//(line_num_words-1)
            first_word_index_without_extra_space = total_extra_spaces%(line_num_words-1) # index for the word after which no extra space should be inserted
        else:
            min_spaces = 0
            first_word_index_without_extra_space = 0
        
        line = ""
        for i in range(left, right+1):
            line += words[i]
            if i != right:
                line += " "*(min_spaces + ((i-left)<first_word_index_without_extra_space))
        return line
        
    def justify_last_line(self, left, line_min_char_count, words, maxWidth):
        line = ""
        for i in range(left, len(words)):
            line += words[i]
            if i != len(words) -1:
                line += " "
        line += " "*(maxWidth - line_min_char_count)
        return line
    
    def justify_single_word_line(self, left, line_min_char_count, words, maxWidth):
        line = words[left]
        line += " "*(maxWidth - line_min_char_count)
        return line
      
 '''
 loop through the words, find the left and right indexes of the words that fit a line. then justify the lines
 '''
