from aigpy import fileHelper


class CheckTool(object):
    def __init__(self):
        self.paths = []

    def is_in_error(self, index, error_index):
        for i in error_index:
            if i == index:
                return True
        return False

    def clear(self):
        self.paths = []

    def add_path(self, path):
        self.paths.append(path)

    def check_paths(self):
        index = 0
        flag = False
        err_index = []
        for path in self.paths:
            if fileHelper.getFileSize(path) <= 0:
                err_index.append(index)
                flag = True
            index = index + 1
        return flag, err_index
