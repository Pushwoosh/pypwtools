from helpers.csv import Row


class Device:
    hwid = ""
    user_id = ""
    push_token = ""
    platform = 0
    tags = {}

    def __str__(self):
        ret = ""
        if self.hwid != "":
            ret += "hwid: " + self.hwid + "\n"

        if self.user_id != "":
            ret += "user id: " + self.user_id + "\n"

        if self.push_token != "":
            ret += "push_token: " + self.push_token + "\n"

        if self.platform != "":
            ret += "type: " + str(self.platform) + "\n"

        if len(self.tags) > 0:
            ret += "tags: \n"
            for tag in self.tags:
                ret += "  " + tag + ": " + self.tags[tag] + "\n"

        return ret


def from_row(row: Row) -> Device:
    ret = Device()
    ret.hwid = row.hwid()
    ret.user_id = row.user_id()
    ret.push_token = row.push_token()
    ret.platform = row.type()
    ret.tags = row.tags()
    return ret
