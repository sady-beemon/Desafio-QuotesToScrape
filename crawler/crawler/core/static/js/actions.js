function startmessage () {
    let items = $('.form-check-input').size();
    selectedStatus.innerText = `Select 0 out of ${items-1} objects`
}

function checkclick () {
    let items = $('.form-check-input').length;
    let selectedvalue = $('.form-check-input:checked').length;
    if ($("#flexCheckDefaultmaster-checkbox").is(":checked")){
        selectedvalue-=1
    }
    selectedStatus.innerText = `Select ${selectedvalue} out of ${items-1} objects`;
    $("#selectAll").prop("value","");

    allowSelectAll(selectedvalue,items);
}


function mastercheckboxclick () {

    let items = $('.form-check-input').length;
    $('input:checkbox').not(this).prop('checked', $("#flexCheckDefaultmaster-checkbox").is(":checked"));
    let selectedvalue = $('.form-check-input:checked').length;
    if ($("#flexCheckDefaultmaster-checkbox").is(":checked")){
        selectedvalue-=1
    }
    selectedStatus.innerText = `Select ${selectedvalue} out of ${items-1} objects`;
    $("#selectAll").prop("value","");

    allowSelectAll(selectedvalue,items);
}

function allowSelectAll (selectedvalue,items) {
    if (selectedvalue === (items-1)) {
        selectAllInput.innerText = `:Select All objects` ;    
    }
    else {
        selectAllInput.innerText = `` ;
    }

}

function selectAll () {
    if(selectAllInput.innerText = `:Select All objects`){

        selectedStatus.innerText = `All objects selected`
        selectAllInput.innerText = `:deSelect All objects`
        $("#selectAll").prop("value","yes")
    }
}

$(document).ready(function(){

    startmessage()

})


$('.form-check-input').on("click", function() {

    checkclick();
} ) ;

$("#flexCheckDefaultmaster-checkbox").on("click", function() {
    mastercheckboxclick();
} ) ;

$("#selectAllInput").on("click", function() {
    if (selectAllInput.innerText == `:Select All objects`) {
        selectAll();
    }
    else {
        selectAllInput.innerText = `:Select All objects` ;  
        $("#selectAll").prop("value","");
        $("#flexCheckDefaultmaster-checkbox").prop('checked',false);
        mastercheckboxclick();
    }
} ) ;

