from app.view_models.book import BookViewModel
class MyWish():
    def __init__(self,id,book,wishes_count):
        self.id=id
        self.book=book
        self.wishes_count=wishes_count
class MyWishes():
    def __init__(self,gifts_of_mine,wish_list):
        self.gift_list=[]
        self.__gifts_of_mine=gifts_of_mine
        self.__wish_list=wish_list
        self.gift_list=self.__parse()
    def __parse(self):
        temp_list=[]
        for gift in self.__gifts_of_mine:
            my_gift=self.__one_to_parse(gift)
            temp_list.append(my_gift)
        return temp_list
    def __one_to_parse(self,gift):
        wish_count=0
        for wish in self.__wish_list:
            if wish['isbn']==gift.isbn:
                wish_count=wish['count']
                break
        my_gift=MyWish(gift.id,BookViewModel(gift.book),wish_count)
        return my_gift