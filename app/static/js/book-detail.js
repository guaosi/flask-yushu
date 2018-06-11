

$(document).on('confirmation', '.remodal', function () {
    var isbn = $('#isbn').text()
    window.location.href='/gifts/book/' + isbn
});