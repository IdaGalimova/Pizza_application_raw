var total_pepperoni = 0;
total_pepperoni = parseInt(total_pepperoni)

function adding_pepperoni_amount(value) {
    total_pepperoni = parseInt(value) + total_pepperoni;
    if (total_pepperoni < 0) {
        total_pepperoni = 0;
    }

    var json_pepperoni = { 
        "Pepperoni": total_pepperoni
    
    }
    if (total_pepperoni != 0) {
        $.ajax({
            url: '/returnjsonPepperoni',
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

var total_quatro_formaggi = 0;
total_quatro_formaggi = parseInt(total_quatro_formaggi)

function adding_quatro_formaggi_amount(value) {
    total_quatro_formaggi = parseInt(value) + total_quatro_formaggi;
    if (total_quatro_formaggi < 0) {
        total_quatro_formaggi = 0;
    }

    var json_quatro_formaggi = { "Quatro Formaggi": total_quatro_formaggi }
    if (total_quatro_formaggi != 0) {
        $.ajax({
            url: '/returnjsonQuatroFormaggi',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(json_quatro_formaggi),

            success: function (response) {
                $('#main').text(response)
            }
        })
    }

    document.getElementById('quatro_formaggi_amount').innerHTML = total_quatro_formaggi;
}


var total_prosciutto_crudo = 0;
total_prosciutto_crudo = parseInt(total_prosciutto_crudo)

function adding_prosciutto_crudo_amount(value) {
    total_prosciutto_crudo = parseInt(value) + total_prosciutto_crudo;
    if (total_prosciutto_crudo < 0) {
        total_prosciutto_crudo = 0;
    }

    var json_prosciutto_crudo = { "Prosciutto Crudo": total_prosciutto_crudo }
    if (total_prosciutto_crudo != 0) {
        $.ajax({
            url: '/returnjsonProsciuttoCrudo',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(json_prosciutto_crudo),

            success: function (response) {
                $('#main').text(response)
            }
        })
    }

    document.getElementById('prosciutto_crudo_amount').innerHTML = total_prosciutto_crudo;
}


var total_quatro_carni = 0; 
total_quatro_carni = parseInt(total_quatro_carni)

function adding_quatro_carni_amount(value) {
    total_quatro_carni = parseInt(value) + total_quatro_carni;
    if (total_quatro_carni < 0) {
        total_quatro_carni = 0;
    }
    // console.log(total_hawaii)
    var json_quatro_carni = { "Quatro Carni": total_quatro_carni }
    if (total_quatro_carni != 0) {
        $.ajax({
            url: '/returnjsonQuatroCarni',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(json_quatro_carni),

            success: function (response) {
                $('#main').text(response)
            }
        })
    }

    document.getElementById('quatro_carni_amount').innerHTML = total_quatro_carni;
}

var total_della_casa = 0; 
total_della_casa = parseInt(total_della_casa)

function adding_della_casa_amount(value) {
    total_della_casa = parseInt(value) + total_della_casa;
    if (total_della_casa < 0) {
        total_della_casa = 0;
    }

    var json_della_casa = { "Della Casa": total_della_casa }
    if (total_della_casa != 0) {
        $.ajax({
            url: '/returnjsonDellaCasa',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(json_della_casa),

            success: function (response) {
                $('#main').text(response)
            }
        })
    }
    document.getElementById('della_casa_amount').innerHTML = total_della_casa;
 }


var total_napoli = 0;
total_napoli = parseInt(total_napoli)

function adding_napoli_amount(value) {
    total_napoli = parseInt(value) + total_napoli;
    if (total_napoli < 0) {
        total_napoli = 0;
    }

    var json_napoli = { 
        "Napoli": total_napoli
    }
    if (total_napoli != 0) {
        $.ajax({
            url: '/returnjsonNapoli',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(json_napoli),

            success: function (response) {
                $('#main').text(response)
            }
        })
    }
    document.getElementById('napoli_amount').innerHTML = total_napoli;
}