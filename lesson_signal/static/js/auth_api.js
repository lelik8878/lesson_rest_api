
let submitButton = document.getElementById('submit');
    submitButton.addEventListener('click', getTokenData)
function getTokenData() {
        let ourLogin = document.getElementById('login')
        let ourPassword = document.getElementById('password')
        fetch('http://127.0.0.1:8000/api/token/',
    {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({username: ourLogin.value, password: ourPassword.value})
    }) .then(response=> {
        if (response.ok) {
            return response.json()
        }
        else {
            let body = document.getElementById('body');
            body.innerHTML += '<h3> Неверный логин или пароль </h3>';
            throw new Error('Error while token ')
        }
        }) .then(tokenData=>{
            console.log(tokenData)
            let body = document.getElementById('body');
            body.innerHTML = '<h3> Hello, Johan!</h3>';
        })
}

