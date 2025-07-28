# Essa é uma solução pouquíssimo otimizada. Existe uma forma EXTREMAMENTE mais simples e otimizada de se fazer isso, e não é nada complicado. O detalhe está na seleção de um ponteiro/indexador do ponto inicial de um morro/vale.

def countHillValley(nums):
    """
        :type nums: List[int]
        :rtype: int
    """
    count = 0
    n = len(nums)
    if n < 3: return 0

    i, j = 0, 2

    while i != j and j < n:
        while j < n and nums[j-1] == nums[j]:
            j += 1
        while i < j and nums[i] == nums[i+1]:
            i += 1
        
        if j == n: return count

        if j-1 == i and j+1 < n:
            j += 1
            while nums[j-1] == nums[j]:
                j += 1
                

        if nums[i] < nums[j-1] > nums[j]:
            count += 1
        if nums[i] > nums[j-1] < nums[j]:
            count += 1
        i, j = i+1, j+1

        if j >= n: return count

    
    return count

print(countHillValley([44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,40,40]))
