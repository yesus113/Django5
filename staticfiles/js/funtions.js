function message_error(obj) {
    var html = ''
    if (typeof (obj) === 'object') {
        html = '<ul style="text-align: left;">';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ':' + value + '</li>';
        });
        html += '</ul>';
    } else {
        html = '<p>' + obj + '</p>';
    }

    Swal.fire({
        icon: "error",
        title: "Error!",
        html: html
    });
}

function Alert_JQueryConfirm() {
    $.confirm({
        title: ' Confirmacion',
        theme: 'material',
        icon: 'fa fa-info',
        columnClass: 'small',
        content: '¿Esta seguro de realizar la siguiente accion?',
        buttons: {
            confirm: function () {
                $.alert('Confirmed!');
            },
            cancel: function () {
                $.alert('Canceled!');
            },
            somethingElse: {
                text: 'Something else',
                btnClass: 'btn-blue',
                keys: ['enter', 'shift'],
                action: function () {
                    $.alert('Something else?');
                }
            }
        }
    });
}