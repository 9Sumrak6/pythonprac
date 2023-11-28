while s := input():
    match s.split():
        case ['mov', a, b]:
            print(f"moving {b} to {a}")
        case ['push' | 'pop' as cmd, *args]:
            print(f"{cmd}ing", *args)
        case [a, b]:
            print(f"making {a} with {b}")
        case _:
            print("Parse error")
