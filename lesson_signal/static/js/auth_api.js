
let submitButton = document.getElementById('submit');
    submitButton.addEventListener('click', getTokenData)
let input = document.createElement('input')
input.type = 'button'
input.value = 'JohanMessage'
input.addEventListener('click', getMessageJohan)

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
            throw new Error('Error while token receiving')
        }
        }) .then(tokenData=>{
            console.log(tokenData)
            localStorage.setItem('access', tokenData.access);
            localStorage.setItem('refresh', tokenData['refresh']);
            let body = document.getElementById('body');
            // body.innerHTML = '<h3> Hello, Johan!</h3><br><input type="button" value="Get data" id="dataButton">';
            body.append(input)
            // let dataButton = document.getElementById('dataButton')
            // dataButton.addEventListener('click', getMessageJohan)
        })
}
function getMessageJohan(){
        console.log('Hello, Alex')
        let accessToken = localStorage.getItem('access')
        fetch('http://127.0.0.1:8000/stadium_api/people_category/',
            {method: 'GET',
            headers: {
                'Authorization': 'Bearer ' + accessToken
            }}) .then(response => {
                if (response.status === 401) {
                    fetch('http://127.0.0.1:8000/api/token/refresh/',
                        {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({refresh: localStorage.getItem('refresh')})
                }
                        ) .then(refResp => refResp.json())
                            .then(data => {
                                localStorage.setItem('access', data.access)
                                console.log('Сменили access')
                            })
                    alert('Произошла смена токена, нажми ещё раз')
                    return response
                }
                else { return response.json()}

            })
            .then(data => {
                console.log(data)
                document.body.innerHTML = `<p>${data.message}</p>`
                document.body.append(input)
            })
}
