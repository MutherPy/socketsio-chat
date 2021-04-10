import {create_message, check_room, user_storage} from "./utils.js";

let room = check_room()
let server_address = `ws://${window.location.hostname}:8003`;
if (room){
    server_address += `?room=${room}`
}

let socket = io(server_address, {
    auth: {
        'token': localStorage.getItem('jwt')
    }
});

let msg_area = document.getElementById('chat_area')
let msg_form = document.getElementById('message_form')
let files_form = document.getElementById('files_form')

socket.on('ready', (msg) => {
    console.log('ready', msg)
    user_storage(msg.sid, msg.username)
})

socket.on('msg', (msg) => {
    msg_area.appendChild(create_message(msg))
})

msg_form.getElementsByTagName('button')[0].addEventListener(
    'click',
    function (e) {
    e.preventDefault()
    let message = this.parentElement['message']
    socket.emit('msg', message.value)
    message.value = ''
    message.focus()
})

files_form.getElementsByTagName('button')[0].addEventListener(
    'click',
    function (e) {
    e.preventDefault()
    let data = new FormData(this.parentElement)
    let file_request = new XMLHttpRequest()

    file_request.onreadystatechange = function () {
        if (file_request.readyState === XMLHttpRequest.DONE) {
            files_form['file'].value = ''
            let file_token = JSON.parse(file_request.responseText)['file_token']
            let full = new URL('download', window.location.origin)
            full.searchParams.append('token', file_token)
            alert(full)
            socket.emit('msg', full.toString())
        }
    }

    let file_post_url = new URL("/chat/sharing_file", window.location.origin)
    file_post_url.searchParams.append('room', room)
    file_request.open("POST", file_post_url.toString())
    socket.emit('sharing')
    file_request.send(data)
})

