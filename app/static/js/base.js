(function () {
    url = window.location.pathname
    if (url == '/my/gifts'){
        $('#gifts').addClass('linking')
    }
    if (url == '/'){
        $('#recent').addClass('linking')
    }
    if (url== '/my/gifts'){
        $('#gifts').addClass('linking')
    }
    if (url == '/my/wish'){
        $('#wishes').addClass('linking')
    }
    if (url == '/pending'){
        $('#pending').addClass('linking')
    }
})()