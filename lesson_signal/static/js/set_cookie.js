
let submitButton = document.getElementById('submit')
    submitButton.addEventListener('click', setManualCookie)

function setManualCookie() {
    let setCookieLogin = document.getElementById('login_cookie')
    let setCookiePassword = document.getElementById('password_cookie')
    fetch('http://127.0.0.1:8000/api/token/',
        {method: 'POST',
            headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',},
            // credentials: 'include',
            body: JSON.stringify({username: setCookieLogin.value, password: setCookiePassword.value})} )
        .then(Response => {
            return Response.json()
        }) .then(tokenData => {
            console.log(tokenData)
        console.log(document.cookie)
    })
}

let withCookieButton = document.getElementById('send_with_cookie')
    withCookieButton.addEventListener('click', getAlex)

function getAlex() {
    fetch('http://127.0.0.1:8000/set_cookie_lesson_drf/',
        {method: 'GET',
            credentials: 'include',
        headers:{
            'Content-Type': 'application/json',
        }
        }) .then(response => response.json())
                .then(alex => console.log(alex))
}

