

import app

def print_app2():
    name = (__name__)
    return name

if __name__ == "__main__":
    # The following is calling code from within this script
    print("I am running code from {0}".format(print_app2()))

    # The following is calling code from the imported app.py
    print("I am running code from {0}".format(app.print_app()))
