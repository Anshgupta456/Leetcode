class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        int_to_str = [str(int) for int in digits]
        str_of_ints = "".join(int_to_str)
        n = int(str_of_ints) + 1
        m = str(n)
        digits = list(m)
        return (digits)