$(document).ready(function () {
    console.log("ready!");
    var alarmtickets_table = $('#alarmtickets').DataTable({
        order: [[5, 'asc'], [ 0, 'desc' ]],
        pageLength: 50
    });

    $(function () {
        $("[data-toggle='tooltip']").tooltip();
    });

    $('input').iCheck({
        checkboxClass: 'icheckbox_square-blue',
        radioClass: 'iradio_square-blue',
        increaseArea: '20%' // optional
    });

    $(".status-filter").on('ifChecked ifUnchecked', function (event) {
        var that = this;
        $(".status-filter").each(function (index) {
            if (index != $(that).attr("id")) {
                $(this).iCheck('uncheck');
            }
        });
        if (event.type == 'ifChecked') {
            $(that).iCheck('check');
            filter_stat = $(that).val();
        } else {
            $(that).iCheck('uncheck');
            filter_stat = "";
        }
        alarmtickets_table.columns(5).search(filter_stat).draw();
    });
});