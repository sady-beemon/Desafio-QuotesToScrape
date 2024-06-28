const mastercheckbox = document.getElementById("flexCheckDefault top-checkbox")
const selectedStatus = document.getElementById("selectedStatus")
const checkboxes = document.getElementsByClassName('form-check-input')


let selectedvalue = 0
let items = 0

for(let checkbox of checkboxes) {
    
    items += 1
    checkbox.onclick = () => {
        if (checkbox.checked) {
            selectedvalue += 1;
        }
        else {
            selectedvalue -= 1;
        }
        selectedStatus.innerText = `Select ${selectedvalue} out of ${items-1} objects`
    }

    selectedStatus.innerText = `Select ${selectedvalue} out of ${items-1} objects`
}


mastercheckbox.onclick = () => {

    let items = 0

    for(let checkbox of checkboxes) {
        items += 1
        if (mastercheckbox.checked) {
            checkbox.checked = true;
            selectedvalue = items-1;
        }
        else {
            checkbox.checked = false;
            selectedvalue = 0
        }
    }

    selectedStatus.innerText = `Select ${selectedvalue} out of ${items-1} objects`
}