$(function () {
    $('#data').DataTable(
        {
            responsive: true,
            autoWidth: true,
            destroy: true,
            deferRender: true, // Carga de datos mas rapida, +50,000
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                data: {'action': 'searchdata'},// parametros
                dataSrc: "",

            },
            columns: [
                {"data": "id"},
                {"data": "name"},
                {"data": "desc"},
                {"data": "desc"},
            ],
            columnDefs: [
                {
                    targets: [2],
                    className: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a href="/core/category/edit/' + row.id + '/" type="button" class="btn btn-primary"><i class="fa-solid fa-pen-to-square"></i></a>';
                        buttons += '<a href="/core/category/delete/' + row.id + '/" type="button" class="btn btn-danger"><i class="fa-solid fa-trash"></i></a>';
                        return buttons;
                    }
                }
            ],
            initComplete: function (settings, json) {
                // alert('Bienvenido');
            }
        }
    );

});