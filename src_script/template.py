class template_AT(object):
    def print_header(self):
        print "Content-type: text/html\n\n"
        print
        print "<html>"
        print "<head>"
        print '<meta charset="UTF-8">'
        print '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
        print '<meta http-equiv="X-UA-Compatible" content="ie=edge">'
        print "<title>Alarm ticket</title>"
        # <!-- css -->
        print '<link rel="stylesheet" href="css/app.css">'
        # <!-- Bootstrap 3.3.7 -->
        print '<link rel="stylesheet" href="AdminLTE-2.4.2/bower_components/bootstrap/dist/css/bootstrap.min.css">'
        # <!-- DataTables -->
        print '<link rel="stylesheet" href="AdminLTE-2.4.2/bower_components/datatables.net-bs/css/dataTables.bootstrap.min.css">'
        # <!-- Font Awesome -->
        print '<link rel="stylesheet" href="AdminLTE-2.4.2/bower_components/font-awesome/css/font-awesome.min.css">'
        # <!-- Ionicons -->
        print '<link rel="stylesheet" href="AdminLTE-2.4.2/bower_components/Ionicons/css/ionicons.min.css">'
        # <!-- jvectormap -->
        print '<link rel="stylesheet" href="AdminLTE-2.4.2/bower_components/jvectormap/jquery-jvectormap.css">'
        # <!-- Theme style -->
        print '<link rel="stylesheet" href="AdminLTE-2.4.2/dist/css/AdminLTE.min.css">'
        # <!-- AdminLTE Skins. Choose a skin from the css/skins
        #    folder instead of downloading all of them to reduce the load. -->
        print '<link rel="stylesheet" href="AdminLTE-2.4.2/dist/css/skins/_all-skins.min.css">'
        # <!-- iCheck -->
        print '<link rel="stylesheet" href="AdminLTE-2.4.2/plugins/iCheck/all.css">'
        # <!-- css in alarm ticket content -->
        print '<link rel="stylesheet" href="css/alarm_ticket.css">'

        print "</head>"
        print "<body>"

    def print_menu(self):
        print '<nav class="navbar-default">'
        print '<div class="container-fluid">'
        print '<div class="navbar-header">'
        print '<a class="navbar-brand" href="index.py">Alarm Ticket</a>'
        print "</div>"
        print '<ul class="nav navbar-nav">'
        # print '<li class="active"><a href="/home">Home</a></li>'
        # print '<li><a href="/splunk">Splunk</a></li>'
        print "</ul>"
        print "</div>"
        print "</nav>"

    def print_close(self):
        print '<script src="js/app.js"></script>'
        print '<script src="js/main.js"></script>'
        # <!-- jQuery 3 -->
        print '<script src="AdminLTE-2.4.2/bower_components/jquery/dist/jquery.min.js"></script>'
        print '<script src="js/jquery-3.3.1.min.js"></script>'
        # <!-- Bootstrap 3.3.7 -->
        print '<script src="AdminLTE-2.4.2/bower_components/bootstrap/dist/js/bootstrap.min.js"></script>'
        # <!-- DataTables -->
        print '<script src="AdminLTE-2.4.2/bower_components/datatables.net/js/jquery.dataTables.min.js"></script>'
        print '<script src="AdminLTE-2.4.2/bower_components/datatables.net-bs/js/dataTables.bootstrap.min.js"></script>'
        # <!-- FastClick -->
        print '<script src="AdminLTE-2.4.2/bower_components/fastclick/lib/fastclick.js"></script>'
        # <!-- AdminLTE App -->
        print '<script src="AdminLTE-2.4.2/dist/js/adminlte.min.js"></script>'
        # <!-- Sparkline -->
        print '<script src="AdminLTE-2.4.2/bower_components/jquery-sparkline/dist/jquery.sparkline.min.js"></script>'
        # <!-- SlimScroll -->
        print '<script src="AdminLTE-2.4.2/bower_components/jquery-slimscroll/jquery.slimscroll.min.js"></script>'
        # <!-- iCheck -->
        print '<script src="AdminLTE-2.4.2/plugins/iCheck/icheck.min.js"></script>'
        print "</body>"
        print "</html>"