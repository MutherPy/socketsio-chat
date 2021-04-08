export {create_message, check_room, user_storage}

let user_storage = function (sid, name=''){
    let username = window.sessionStorage.getItem(sid)
    if (username === null){
        window.sessionStorage.setItem(sid, name)
        username = name
    }
    return username
}

let create_message = function (msg) {
    let block = document.createElement('div')
    block.classList.add('chat_window_row')
    let username = document.createElement('span')
    username.innerText = user_storage(msg.sid)
    block.appendChild(username)
    let msg_text = document.createElement('span')
    msg_text.innerText = msg['text']
    block.appendChild(msg_text)
    return block
}

let check_room = function () {
    const urlParams = new URLSearchParams(window.location.search)
    return urlParams.get('room')
}