def builddir_del_err(i, path, j):
    from functions.message import message # REMOVE AT PACKAGING
    message("error", f"Path '{path}' was unable to be deleted.")
    exit(1)
