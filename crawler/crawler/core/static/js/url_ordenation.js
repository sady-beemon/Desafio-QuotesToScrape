function setParam(url, paramName, paramValue) {

    let urlObj = new URL(url);
    
    let params = new URLSearchParams(urlObj.search);
    
    params.set(paramName, paramValue);
    
    urlObj.search = params.toString();
    
    return urlObj.toString();
}

function mantainElementOrder (element, elementname) {
    
    fieldURL = $(location).attr('href')
    ordenationHTML = ""

    if (fieldURL.includes("-" + element.attr('name').split("header_element_")[1])) {
        ordenationHTML = "&uarr;"
    }
    else if (fieldURL.includes(element.attr('name').split("header_element_")[1])) {
        ordenationHTML = "&darr;"
    }

    elementname.innerHTML += ordenationHTML;
}

function setHeaderUrl (URL, value) {
    let newURL
    newURL = setParam(URL, "o",value)

    return newURL
}


function setHeaderElementOrder (element, elementname) {
    
    fieldURL = $(location).attr('href')
    value = ""

    if (fieldURL.includes((element.attr('name').split("header_element_")[1])) == false) {
        value = (element.attr('name').split("header_element_")[1])
    }
    else if (fieldURL.includes("-" + element.attr('name').split("header_element_")[1])) {
        value = ""
    }
    else {
        value = ("-" + element.attr('name').split("header_element_")[1])
    }

    fieldURL = setHeaderUrl(fieldURL,value)
    element.attr("href", fieldURL)

}

$(document).ready(function(){

    mantainElementOrder($("#header_element_rank"), header_element_rank);
    mantainElementOrder($("#header_element_title"), header_element_title);
    mantainElementOrder($("#header_element_date"), header_element_date);
    mantainElementOrder($("#header_element_time"), header_element_time);
    mantainElementOrder($("#header_element_minage"), header_element_minage);
    mantainElementOrder($("#header_element_score"), header_element_score);

})


$("#header_element_rank").on("click", function() {
    setHeaderElementOrder($("#header_element_rank"), header_element_rank);
});

$("#header_element_title").on("click", function() {
    setHeaderElementOrder($("#header_element_title"), header_element_title);
});

$("#header_element_date").on("click", function() {
    setHeaderElementOrder($("#header_element_date"), header_element_date);
});

$("#header_element_time").on("click", function() {
    setHeaderElementOrder($("#header_element_time"), header_element_time);
});

$("#header_element_minage").on("click", function() {
    setHeaderElementOrder($("#header_element_minage"), header_element_minage);
});

$("#header_element_score").on("click", function() {
    setHeaderElementOrder($("#header_element_score"), header_element_score);
});