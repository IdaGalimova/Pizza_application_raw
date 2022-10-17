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
