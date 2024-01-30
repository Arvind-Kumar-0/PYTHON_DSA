if not root:
    return []
q = collections.deque()
q.append(root)

ans = []
while q:
    for _ in range(len(q)):
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    ans.append(node.val)
return ans
