from app.lib.enums import PendingStatus


class DriftViewModel():
    def __init__(self,drift,current_user_id):
        self.data={}
        self.data=self.__parse(drift,current_user_id)
    def __parse(self,drift,current_user_id):
        you_are=DriftViewModel.is_requester_or_gift(drift,current_user_id)
        status_str=PendingStatus.pending(drift.pending,you_are)
        r={
            'you_are':you_are,
            'drift_id':drift.id,
            'book_title':drift.book_title,
            'book_author':drift.book_author,
            'book_img':drift.book_img,
            'date':drift.create_datetime.strftime('%Y-%m-%d'),
            'message':drift.message,
            'address':drift.address,
            'operator':drift.gifter_name if you_are=='requester' else drift.requester_name,
            'recipient_name':drift.recipient_name,
            'mobile':drift.mobile,
            'status':drift.pending,
            'status_str':status_str
        }
        return r
    @staticmethod
    def is_requester_or_gift(drift,uid):
        return 'requester' if drift.requester_id==uid else 'gifter'
class DriftCollection():
    def __init__(self,drifts,current_user_id):
        self.data=[]
        self.__parse(drifts,current_user_id)
    def __parse(self,drifts,current_user_id):
        for drift in drifts:
            temp=DriftViewModel(drift,current_user_id)
            self.data.append(temp.data)