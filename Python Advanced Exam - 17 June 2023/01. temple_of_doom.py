from collections import deque

tools = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances:
    current_tool = tools.popleft()
    current_sub = substances.pop()

    result = current_tool * current_sub

    for challenge in challenges:
        if result == challenge:
            challenges.remove(challenge)
            break

    else:
        current_tool += 1
        tools.append(current_tool)
        current_sub -= 1

        if current_sub > 0:
            substances.append(current_sub)

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join([str(tool) for tool in tools])}")

if substances:
    print(f"Substances: {', '.join([str(sub) for sub in substances])}")

if challenges:
    print(f"Challenges: {', '.join([str(chal) for chal in challenges])}")





