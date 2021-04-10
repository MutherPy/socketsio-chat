let form = document.getElementById('entering_form')

form.onsubmit = function (ev){
    ev.preventDefault()
    if (form['username'].value !== ''){

        let xhr = new XMLHttpRequest()
        xhr.onreadystatechange = function (){
            if (xhr.readyState === XMLHttpRequest.DONE) {
                let token = JSON.parse(xhr.responseText)['token']
                console.log(token)
                localStorage.setItem('jwt', token);
                if (form['room'].value){
                    window.location.href = window.location.origin + "/chat" + `?room=${form['room'].value}`
                }
                else {
                    window.location.href = window.location.origin + "/chat"
                }
            }
        }
        xhr.open('POST', '/login')
        xhr.send(new FormData(this))
    }
}