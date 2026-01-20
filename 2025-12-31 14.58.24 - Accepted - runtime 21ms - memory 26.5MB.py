class Solution:
    def stringSequence(self, target: str) -> List[str]:
        result = []
        current = ""
        
        for char in target:
            # First, append 'a' to current string
            current += 'a'
            result.append(current)
            
            # Then change last character until we reach target char
            while current[-1] != char:
                # Increment last character
                current = current[:-1] + chr(ord(current[-1]) + 1)
                result.append(current)
        
        return result