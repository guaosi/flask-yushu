from enum import Enum
class PendingStatus(Enum):
    Waiting=1
    Success=2
    Reject=3
    Redraw=4
    @classmethod
    def pending(cls,status,key):
        key_map={
            cls.Waiting:{
                'requester':'等待对方邮寄',
                'gifter':'等待你邮寄'
            },
            cls.Success: {
                'requester': '对方已邮寄',
                'gifter': '你已邮寄'
            },
            cls.Reject: {
                'requester': '对方已拒绝',
                'gifter': '你已拒绝'
            },
            cls.Redraw: {
                'requester': '你已撤销',
                'gifter': '对方已撤销'
            }
        }
        return key_map[status][key]