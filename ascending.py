def stop_ascending(n):
    if not n:
        return None
    for i in range(1,len(n)):
        if n[i]<=n[i-1]:
            return i
    return len(n)