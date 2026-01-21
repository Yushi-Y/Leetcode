# (Medium) 609. Find Duplicate File in System [Anthropic]

# Logic: parse the path to be dire/file_name, remove the file content
# Then create a dictionary, where key is each file content, value is list of parsed path with that file content
# For every key that has a value with more than one entry, return that value (list)

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = {}

        for path in paths:
            parts = path.split(" ")
            dir_path = parts[0] # root/d1/d2
            for remaining_part in parts[1:]:
                file_name, content = remaining_part.split("(")
                content = content[:-1] # remove the ")"
                full_path = dir_path + "/" + file_name
                
                if content not in content_map:
                    content_map[content] = []
                content_map[content].append(full_path)
            
        result = []
        for files in content_map.values():
            if len(files) > 1:
                result.append(files)

        return result
