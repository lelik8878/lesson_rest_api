
confirm('Fill this form, Johan')

const inputList = document.querySelectorAll(`#send_data_form input`)
const new_button = document.querySelector(`#send_data_form button`)

function add_to_json() {
    const new_json = JSON.stringify({
        name: inputList[1].value,
        price: inputList[2].value,
        image: inputList[3].files[0]
    })
    fetch('http://127.0.0.1:8000/api/save_to_db/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': inputList[0].value,
        },
        body: new_json,
    })
        .then(response => response.json())
        .then(data => console.log(data))
}
console.log(inputList)
console.log(new_button)
new_button.addEventListener('click', add_to_json)