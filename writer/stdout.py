class ConsoleWriter(object):
    def __init__(self, first_line, col_order, col_name_dict):
        self.first_line = first_line
        self.col_order = col_order
        self.col_name_dict = col_name_dict

    def _gen_row(self, result):
        row = ""
        for col in self.col_order:
            row = row + "{:<30}".format(result[col])
        return row

    def write(self, output):
        print("\n\n\n" + self.first_line + "\n\n")
        print(self._gen_row(self.col_name_dict) + "\n")
        for result in output:
            print(self._gen_row(result))
