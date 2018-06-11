
function getAllFormFields(formID){
    var fields = {}
    var target = $('#' + formID).serializeArray()
    $.each(target, function() {
      fields[this.name] = this.value
    })
    return fields
}


function getQueryString(name)
{
     var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
     var r = window.location.search.substr(1).match(reg);
     if(r!=null)return  unescape(r[2]); return null;
}

(function (){
    console.log(window.history.length)
})()

