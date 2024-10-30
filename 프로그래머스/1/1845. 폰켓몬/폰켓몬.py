def solution(nums):
    n = len(nums) // 2
    pokemon = set()
    for num in nums:
        pokemon.add(num)
    return min(len(pokemon), n)