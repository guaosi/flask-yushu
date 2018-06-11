class HTTP {
    static post(url, data,success,error) {
        $.ajax({
            type: 'POST',
            url: url,
            data:data,
            success:success,
            error:error,
            headers: {
                Accept: 'application/json'
            }
        })
    }

    static get(url, success, error){
        $.ajax({
            type:'GET',
            url:url,
            success:success,
            error:error
        })
    }
}