
def prRed(stmt): print("\033[91m {}\033[00m".format(stmt))
def prGreen(stmt): print("\033[92m {}\033[00m".format(stmt))
def prYellow(stmt, endo): print("\033[93m {}\033[00m".format(stmt), end=endo)
def prLightPurple(stmt): print("\033[94m {}\033[00m".format(stmt))
def prPurple(stmt): print("\033[95m {}\033[00m".format(stmt))
def prCyan(stmt): print("\033[96m {}\033[00m".format(stmt))
def prLightGray(stmt): print("\033[97m {}\033[00m".format(stmt))
def prBlack(stmt): print("\033[98m {}\033[00m".format(stmt))