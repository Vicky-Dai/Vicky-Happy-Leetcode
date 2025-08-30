def simplifyPath(path: str) -> str:
    parts = path.split('/')  # 按 '/' 拆分路径 如果是//或者///，那么自动解析出来空的
    stack = []

    for part in parts:
        if part == '' or part == '.':
            # 空字符串或当前目录，忽略
            continue
        elif part == '..':
            # 返回上一级，如果栈非空则弹出
            if stack:
                stack.pop()
        else:
            # 普通目录名，入栈
            stack.append(part)

    # 最后拼接成以 '/' 开头的路径
    return '/' + '/'.join(stack)
