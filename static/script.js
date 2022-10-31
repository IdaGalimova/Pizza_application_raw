var total_pepperoni = 0;
total_pepperoni = parseInt(total_pepperoni)

function adding_pepperoni_amount(value) {
    total_pepperoni = parseInt(value) + total_pepperoni;
    if (total_pepperoni < 0) {
        total_pepperoni = 0;
    }
    // console.log(total_pepperoni)
    var json_pepperoni = { 
        "Pepperoni": total_pepperoni
    }
    if (total_pepperoni != 0) {
        $.ajax({
            url: '/returnjson1',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(json_pepperoni),

            success: function (response) {
                $('#main').text(response)
            }
        })
    }
    document.getElementById('pepperoni_amount').innerHTML = total_pepperoni;
}

var total_hawaii = 0;
total_hawaii = parseInt(total_hawaii)

function adding_hawaii_amount(value) {
    total_hawaii = parseInt(value) + total_hawaii;
    if (total_hawaii < 0) {
        total_hawaii = 0;
    }
    // console.log(total_hawaii)
    var json_hawaii = { "Hawaii": total_hawaii }
    if (total_hawaii != 0) {
        $.ajax({
            url: '/returnjson2',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(json_hawaii),

            success: function (response) {
                $('#main').text(response)
            }
        })
    }
    console.log(total_hawaii)
    document.getElementById('hawaii_amount').innerHTML = total_hawaii;
}
