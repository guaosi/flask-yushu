class MyGift {

    constructor(isbn) {
        this.isbn = isbn
        this.douban_url = 'https://api.douban.com/v2/book/isbn/' + isbn
    }

    data_from_douban(book_element) {
        this.book_element = book_element
        HTTP.get(this.douban_url, this.when_data_success, this.when_data_error)
    }

    when_data_success(result){
        let c = 1
        // this.$(book_element).('#title').html(result.title)
    }

    when_data_error(errors){
        alert(errors)
    }
}

(function() {
    $('#book').each(function(index, element){
        book_isbn = $(element).data('isbn')
        gift = new MyGift(book_isbn)
        gift.data_from_douban(element)
    })
})()