$(document).ready(function () {
    console.log("ready!");
    $('#alarmtickets').DataTable({
        order: [[6, 'asc'], [ 0, 'desc' ]],
        pageLength: 50
    });
});