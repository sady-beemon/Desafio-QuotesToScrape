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

function setHeaderElementOrder (element, elementname, inputElement) {

    if (element.data('order') == "") {
        element.data('order', '1');
        inputElement.prop("value",(element.attr('name').split("header_element_")[1]));
        elementname.innerHTML = elementname.innerHTML += "&uarr;";
    }
    else if (element.data('order') == "1") {
        element.data('order', '2');
        inputElement.prop("value",("-" + element.attr('name').split("header_element_")[1]));
        elementname.innerHTML = elementname.innerHTML.split("↑",1);
        elementname.innerHTML = elementname.innerHTML += "&darr;";
    }
    else {
        element.data('order', '');
        inputElement.prop("value","");
        elementname.innerHTML = elementname.innerHTML.split("↓",1);
    }

    $("#tableHeaderForm").trigger( "submit" )
    
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

$("#header_element_rank").on("click", function() {
    setHeaderElementOrder($("#header_element_rank"), header_element_rank, $("#input_header_element_rank"));
});

$("#header_element_title").on("click", function() {
    setHeaderElementOrder($("#header_element_title"), header_element_title, $("#input_header_element_title"));
});

$("#header_element_date").on("click", function() {
    setHeaderElementOrder($("#header_element_date"), header_element_date, $("#input_header_element_date"));
});

$("#header_element_time").on("click", function() {
    setHeaderElementOrder($("#header_element_time"), header_element_time, $("#input_header_element_time"));
});

$("#header_element_minage").on("click", function() {
    setHeaderElementOrder($("#header_element_minage"), header_element_minage, $("#input_header_element_minage"));
});

$("#header_element_score").on("click", function() {
    setHeaderElementOrder($("#header_element_score"), header_element_score, $("#input_header_element_score"));
});