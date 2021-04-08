let form = document.getElementById('entering_form')
form.onsubmit = function (ev){
    ev.preventDefault()
    if (form['username'].value !== ''){
        if (form['room'].value){
            window.location.href = window.location.origin + "/chat" + `?room=${form['room'].value}`
        }
        else {
            window.location.href = window.location.origin + "/chat"
        }
    }
}