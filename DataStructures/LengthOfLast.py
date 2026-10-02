class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = s.strip().split()
        return len(ls[-1])
print(Solution().lengthOfLastWord('Hello World'))

#Optimal Space Solution
class Solution:

  def lengthOfLastWord(self, s: str) -> int:
    length = 0
    i = len(s) - 1

    # Skip any trailing spaces
    while i >= 0 and s[i] == ' ':
      i -= 1

    # Count characters of the last word until the next space
    while i >= 0 and s[i] != ' ':
      length += 1
      i -= 1

    return length


print(Solution().lengthOfLastWord('Hello World'))  # Output: 5
print(Solution().lengthOfLastWord('   fly me   to   the moon  '))  # Output: 4