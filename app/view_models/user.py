class UserSummary():
    def __init__(self,user):
        self.nickname=user.nickname
        self.beans=user.beans
        self.email=user.email
        self.send_receive=str(user.send_counter)+'/'+str(user.receive_counter)
class UsersSummary():
    def __init__(self,users):
        self.users=[]
        self.__parse(users)
    def __parse(self,users):
        self.users=[UserSummary(users)]
    @property
    def first(self):
        return self.users[0] if len(self.users) else None;

