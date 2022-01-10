// Datatables

$( document ).ready(function() {

    setTimeout(function () {

        $('#example').DataTable({
            responsive: true
        });

        $('#bank-operation-list').DataTable({
            responsive: true,
            "searching": true,
        });

        $('#menago_table').DataTable({
            responsive: true,
            "searching": true,
        });

        $('#employee_table').DataTable({
            responsive: true,
            "searching": true,
        });

        $('#example2').DataTable({
            scrollY:        '292px',
            scrollCollapse: true,
            paging:         false,
            "searching": false,
            "info": false
        });

    }, 1);

});