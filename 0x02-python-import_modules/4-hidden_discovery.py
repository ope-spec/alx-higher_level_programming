#!/usr/bin/python3
import os.path
if os.path.exists("hidden_4.pyc"):
    os.remove("hidden_4.pyc")

if __name__ == "__main__":
    import hidden_4

    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print("{}".format(name))
