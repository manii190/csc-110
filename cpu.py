def get_result(gigahertz, core_count):
    if core_count >= 20:
        return "That is a high-performance CPU."
    
    if gigahertz >= 3.2 and core_count >= 8:
        return "That is a high-performance CPU."
    
    if gigahertz >= 2.5 and core_count >= 6:
        return "That is a medium-performance CPU."
    
    if gigahertz >= 2.0 and core_count >= 2:
        return "That is a low-performance CPU."

    else  :
        return "That CPU could use an upgrade."
    

def main():
    gigahertz = 2.0
    core_count = 8
    assert get_result(gigahertz, core_count) == "That is a low-performance CPU."

    gigahertz = 4.0
    core_count = 7
    assert get_result(gigahertz, core_count) == "That is a medium-performance CPU."
    print("End of tests")

main()
