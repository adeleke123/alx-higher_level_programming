#!/usr/bin/python3
if __name__ == "__main__":
    """Prints all the names defined by
    the complied module hiden_4.pyc"""
    import hidden_4
    for i in dir(hidden_4):
        if i[:2] != "__":
            print(i)
