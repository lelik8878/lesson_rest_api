
const button = document.querySelector('.button')
console.log(button)
button.addEventListener('click', sendData)
function sendData() {
    const dataStr = {'name': 'String for backend'}
    fetch('http://127.0.0.1:8000/api/products/',
        {
            method: 'POST',
            // body: JSON.stringify(dataStr),
            headers: {
                'Content-Type': 'application/json; charset=utf-8'
            }
        }
    )
        .then(resp => resp.json())
        .then(data => {
            console.log(data)
        })
}

const inputList = document.querySelectorAll(`#send_data_form input`)
const new_button = document.querySelector(`#send_data_form button`)

function add_to_json() {
    const new_json = JSON.stringify({
        product_title: inputList[0].value,
        product_image: inputList[1].value,
        product_price: inputList[2].files[0]
    })
    fetch('http://127.0.0.1:8000/api/save_to_db/', {
        method: 'POST',
        mode: "no-cors",
        headers: {
            'Content-Type': 'application/json'
        },
        body: new_json,
    })
        .then(response => response.json())
        .then(data => console.log(data))
}
console.log(inputList)
console.log(new_button)
new_button.addEventListener('click', add_to_json)