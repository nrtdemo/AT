$(document).ready(function () {
    console.log("ready!");

    startRefresh();
    init_func();

    //Call the functions
    doReport();

    //... then set the interval
    setInterval(doReport, 30000);// Report user presence every 30sec
});

function init_func() {
    var alarmtickets_table = $('#alarmtickets').DataTable();

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
        alarmtickets_table.columns(4).search(filter_stat).draw();
    });

    $("[data-toggle='tooltip']").tooltip();

    $(".dropdown-toggle").dropdown();

    $('input').iCheck({
        checkboxClass: 'icheckbox_square-blue',
        radioClass: 'iradio_square-blue',
        increaseArea: '20%' // optional
    });
}

$('#form_openticket').on('submit', function (e) {
    var request;
    e.preventDefault();

    var $form = $(this);

    // Let's select and cache all the fields
    var $inputs = $form.find("input, select, button, textarea");

    // Serialize the data in the form
    var serializedData = $form.serialize();

    // Disabled form elements will not be serialized.
    $inputs.prop("disabled", true);

    $.ajax({
        type: 'POST',
        url: "./checkvalue.py",
        data: serializedData, //passing some input here
        // dataType: "text",
        success: function (response) {
            alert('success');
            console.log(response);
        }
    }).done(function (data) {
        console.log(data);
        alert(data);
    }).always(function () {
        // Reenable the inputs
        $inputs.prop("disabled", false);
    });

});

function startRefresh() {
    setTimeout(startRefresh, 0.5 * 1000 * 60);
    var search = window.location.search;
    $.get('refresh.py' + search, function (data) {

        if ($.fn.dataTable.isDataTable('#alarmtickets')) {

            table = $('#alarmtickets').DataTable();

            table.clear().draw();
            data.forEach(function (item, index, arr) {
                var css_port_status = "class='text-center'";
                var devicetime = item[9];
                var hostname = item[10];
                var TicketNo = '', catId = '';
                if (item[0] != 'None') {
                    TicketNo = item[0];
                }
                if (item[1].length < 12) {
                    catId = item[1];
                }

                var timenow = new Date() / 1000 | 0;
                var timestamp = new Date(item[11]) / 1000;
                var linkbtn = '';
                if (item[4].toLowerCase() == "down") {
                    css_port_status = "class='port_status_down text-center'"
                    var ddTime = '';
                    if (item[7] == 'Closed' || item[7] == 'None') {
                        if (timenow - timestamp < 30) {
                            ddTime = 'active';
                        } else {
                            ddTime = 'not active';
                        }
                        linkbtn = '<a href="openticket.py?cat_id=' + catId + '"><input type="button" class="btn btn-default" value="open ticket"></a><br/>' + ddTime + '<br/>'
                    }
                } else if (item[4].toLowerCase() == "up") {
                    css_port_status = "class='port_status_up text-center'"
                }

                var jRow = $("<tr>").append(
                    "<td><a href='activity.py?TicketNo=" + TicketNo + "'>" + TicketNo + "</a></td>",
                    "<td>" + catId + "</td>",
                    "<td>" + item[2] + "</td>",
                    "<td><div data-toggle='tooltip' data-placement='bottom' title='" + hostname + "'>" + item[3] + "</div></td>",
                    "<td " + css_port_status + "><div data-toggle='tooltip' data-placement='bottom' title='" + devicetime + "'>" + item[4] + "</div></td>",
                    "<td>" + item[5] + "</td>",
                    "<td>" + item[6] + "</td>",
                    "<td>" + item[7] + "</td>",
                    "<td>" + item[8] + "</td>",
                    "<td>" + linkbtn + "</td>"
                    )
                ;
                table.row.add(jRow).draw();
            });

            resetData(table);
            table.order([4, 'asc'], [0, 'desc']).draw();
            table.page.len(100).draw();
            $("[data-toggle='tooltip']").tooltip();
            table.page.len(50).draw();
        }

    });
}

function resetData(tablename) {
    var table = tablename;
    table.rows().every(function () {
        var d = this.data();

        d.counter++; // update data source for the row

        this.invalidate(); // invalidate the data DataTables has cached for this row
    });
    table.draw();
}

function doReport() {
    var k = getXMLHttpRequestObject();
    if (k != false) {
        url = "src_script/active.py?type=report&CatID=" + document.getElementById("CatID").value;
        k.open("POST", url, true);
        k.onreadystatechange = function () {
            if (k.readyState == 4) {
                //...Do nothing...
            }
        };
        k.send();
    }
    else {
        alert("Cant create XMLHttpRequest");
    }
}

//Getting the right XMLHttpRequest object
function getXMLHttpRequestObject() {
    xmlhttp = 0;
    try {
        // Try to create object for Chrome, Firefox, Safari, IE7+, etc.
        xmlhttp = new XMLHttpRequest();
    }
    catch (e) {
        try {
            // Try to create object for later versions of IE.
            xmlhttp = new ActiveXObject('MSXML2.XMLHTTP');
        }
        catch (e) {
            try {
                // Try to create object for early versions of IE.
                xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');
            }
            catch (e) {
                // Could not create an XMLHttpRequest object.
                return false;
            }
        }
    }
    return xmlhttp;
}