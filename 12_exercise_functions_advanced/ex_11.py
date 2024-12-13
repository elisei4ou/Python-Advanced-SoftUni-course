def math_operations(*nums, **kwargs):
    my_chars = ["a", "s", "d", "m"]
    result = ""
    for i in range(len(nums)):
        char = i % 4
        if my_chars[char] == "a":
            kwargs["a"] += nums[i]
        elif my_chars[char] == "s":
            kwargs["s"] -= nums[i]
        elif my_chars[char] == "d":
            if nums[i] != 0:
                kwargs["d"] /= nums[i]
        elif my_chars[char] == "m":
            kwargs["m"] *= nums[i]
    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    for k, v in kwargs:
        result += f"{k}: {v:.1f}" + "\n"
    return result


print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))