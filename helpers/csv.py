class Struct:
    """
    Struct is a helper class that holds structure of CSV file.
    Can be created from CSV file header using parse_struct function.
    """
    hwid = -1  # hwid column number
    user_id = -1  # user id column number
    push_token = -1  # ...
    type = -1  # ..
    tags = {}  # map [name] => number. column numbers for each tag

    def tag(self, tag: str) -> int:
        if tag in self.tags:
            return self.tags[tag]
        else:
            return -1


def parse_struct(row: list):
    ret = Struct()

    for i, name in enumerate(row):
        if name == "Hwid":
            if ret.hwid == -1:
                ret.hwid = i
                continue
        if name == "User ID":
            if ret.user_id == -1:
                ret.user_id = i
                continue
        if name == "Push Token":
            if ret.push_token == -1:
                ret.push_token = i
                continue
        if name == "Type":
            if ret.type == -1:
                ret.type = i
                continue
        if name == "Type (humanized)":
            pass

        ret.tags[name] = i

    return ret


class Row:
    struct = None
    data = []

    def __init__(self, struct: Struct, data: list):
        self.struct = struct
        self.data = data

    def hwid(self) -> str:
        if self.struct.hwid == -1:
            return ""
        return self.data[self.struct.hwid]

    def user_id(self) -> str:
        if self.struct.user_id == -1:
            return ""
        return self.data[self.struct.user_id]

    def push_token(self) -> str:
        if self.struct.push_token == -1:
            return ""
        return self.data[self.struct.push_token]

    def type(self) -> str:
        if self.struct.type == -1:
            return ""
        return self.data[self.struct.type]

    def tag(self, tag: str) -> str:
        """
        return given tag value
        :param tag:
        :return:
        """
        if tag not in self.struct.tags:
            return ""
        return self.data[self.struct.tags[tag]]

    def tags(self) -> dict:
        """
        return all tags values as dict [name] => value
        :return:
        """
        ret = {}
        for tag in self.struct.tags:
            if tag == 'Type (humanized)':
                continue
            ret[tag] = self.data[self.struct.tags[tag]]
        return ret
