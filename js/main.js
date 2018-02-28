$(document).ready(function () {
    console.log("ready!");
    var alarmtickets_table = $('#alarmtickets').DataTable({
        order: [[6, 'asc'], [ 0, 'desc' ]],
        pageLength: 50
    });

    $('input').iCheck({
        checkboxClass: 'icheckbox_square-blue',
        radioClass: 'iradio_square-blue',
        increaseArea: '20%' // optional
    });

    $(".status-filter").on('ifChecked ifUnchecked', function (event) {
        var that = this;
        if (event.type == 'ifChecked') {
            $(that).iCheck('check');
            filter_stat = $(that).val();
        } else {
            $(that).iCheck('uncheck');
            filter_stat = "";
        }
        alarmtickets_table.columns(6).search(filter_stat).draw();
    });
});