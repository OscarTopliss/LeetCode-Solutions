class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        existing_paths = {}
        current_sub_path = existing_paths
        index = 0
        while index < len(folder):
            item = folder[index]
            split_path = self.splitPath(item)
            if self.insertNestedDictionary(existing_paths, split_path):
                index += 1
                continue
            folder.pop(folder.index(item))
        print(existing_paths)
        return folder    
    
    def splitPath(self, path: str):
        split_paths = path.split("/")
        paths = ["/" + split for split in split_paths]
        paths.pop(0) # removes the "/" path
        return paths
    
    def insertNestedDictionary(self, dictionary: dict, values: List[str]) -> bool:
        current_dictionary = dictionary
        index = 0
        while index < len(values):
            entry = values[index] 
            FINAL = index == len(values) - 1
            if entry in current_dictionary:
                current_dictionary = current_dictionary[entry]
                if "FINAL" in current_dictionary:
                    return False
                index += 1
                continue
            current_dictionary[entry] = {}
            current_dictionary = current_dictionary[entry]
            if FINAL:
                current_dictionary["FINAL"] = True
            index += 1
        return True
