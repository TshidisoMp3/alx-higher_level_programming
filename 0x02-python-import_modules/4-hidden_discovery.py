#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    details = dir(hidden_4)
    for detail in details:
        if detail[:2] != "__":
            print(detail)
