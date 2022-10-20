var total = 0;
total = parseInt(total)

function adding_pepperoni_amount(value) {
    total = parseInt(value) + total;
    if (total < 0) {
        total = 0;
    }
    console.log(total)
    var test = { "pepperoni_amount": total }
    $.ajax({
        url: '/returnjson1',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(test),

        success: function (response) {
            $('#main').text(response)
        }
    })

    document.getElementById('pepperoni_amount').innerHTML = total;
}

var total_hawaii = 0;
total_hawaii = parseInt(total_hawaii)

function adding_hawaii_amount(value) {
    total_hawaii = parseInt(value) + total_hawaii;
    if (total_hawaii < 0) {
        total_hawaii = 0;
    }
    console.log(total_hawaii)
    var json_hawaii = { "hawaii_amount": total_hawaii }
    $.ajax({
        url: '/returnjson2',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(json_hawaii),

        success: function (response) {
            $('#main').text(response)
        }
    })

    document.getElementById('hawaii_amount').innerHTML = total_hawaii;
}
