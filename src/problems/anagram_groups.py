class Solution:
    def groupAnagrams(self, strs):
        anagram_type_map = {}
        anagram_group_list = []
        for string in strs:
            char_count_list = ["" for i in range(26)]
            for char in string:
                char_count_list[ord(char)-ord("a")]+=char
            base_anagram = "".join(char_count_list)
            if anagram_type_map.get(base_anagram) is not None:
                index = anagram_type_map[base_anagram]
                anagram_group_list[index].append(string)
            else:
                anagram_type_map[base_anagram] = len(anagram_group_list)
                anagram_group_list.append([string])
        return anagram_group_list