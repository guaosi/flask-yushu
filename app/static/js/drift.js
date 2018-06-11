
(function (){
    historyLength = window.history.length
    var a = $('#nav_url')
    if (historyLength > 1){
        a.text('返回')
        a.attr('href', '#')
        a.click(function(){
            window.history.back(-1)
        })
    }
    else{
        a.text('去首页')
        a.attr('href', '/')
    }
    console.log(window.history.length)
})()

