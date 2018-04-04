$(document).ready(function () {
    console.log("ready!");
    var alarmtickets_table = $('#alarmtickets').DataTable({
        order: [[4, 'asc'], [0, 'desc']],
        pageLength: 50
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
        alarmtickets_table.columns(4).search(filter_stat).draw();
    });

    $("[data-toggle='tooltip']").tooltip();

    $(".dropdown-toggle").dropdown();

    $('input').iCheck({
        checkboxClass: 'icheckbox_square-blue',
        radioClass: 'iradio_square-blue',
        increaseArea: '20%' // optional
    });

    //Call the functions
    doReport();

    //... then set the interval
    setInterval(doReport, 30000);// Report user presence every 30sec
});


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