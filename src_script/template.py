# <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/dt/dt-1.10.16/datatables.min.css"/>
# <script type="text/javascript" src="https://cdn.datatables.net/v/dt/dt-1.10.16/datatables.min.js"></script>

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
        print '<link rel="stylesheet" href="lib/Bootstrap-3.3.7/css/bootstrap.min.css">'
        # <!-- DataTables -->
        # print '<link rel="stylesheet" href="lib/DataTables-1.10.16/css/dataTables.bootstrap.min.css">'
        print '<link rel="stylesheet" href="lib/datatables.css">'

        # <!-- iCheck -->
        print '<link rel="stylesheet" href="lib/iCheck/skins/all.css">'

        # <!-- css in alarm ticket content -->
        print '<link rel="stylesheet" href="css/alarm_ticket.css">'

        print "</head>"
        print "<body>"

    def print_menu(self):
        print '<nav class="navbar-default">'
        print ' <div class="container-fluid">'
        print '     <div class="navbar-header">'
        print '         <a class="navbar-brand" href="index.py">Alarm Ticket</a>'
        print '     </div>'
        # print '         <a class="navbar-brand" href="PEbangkok.py">Link PE Bangkok Flap 24hr</a>'
        print """
                    <ul class="nav navbar-nav">
                           <li class="dropdown">
                            <a href="#" class="dropdown-toggle navbar-brand" id="myDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> 
                                Bangkok Link<span class="caret"></span></a>
                                <ul class="dropdown-menu" aria-labelledby="myDropdown">
                                    <li><a class="dropdown-item" href="index.py?link=40G100G"> Link 40G&100GbE Up_Down</a></li>
                                    <li><a class="dropdown-item" href="index.py?link=PE">Link PE Bangkok Flap 24hr</a></li>
                                </ul>
                           </li>
                    </ul>
               """
        print " </div>"
        print "</nav>"

    def print_close(self):
        print '<script src="js/app.js"></script>'
        print '<script src="js/main.js"></script>'
        # <!-- jQuery 3 -->
        print '<script src="js/jquery-3.3.1.min.js"></script>'
        # <!-- Bootstrap 3.3.7 -->
        print '<script src="lib/Bootstrap-3.3.7/js/bootstrap.min.js"></script>'
        # <!-- DataTables -->
        # print '<script src="lib/DataTables-1.10.16/js/jquery.dataTables.min.js"></script>'
        # print '<script src="lib/DataTables-1.10.16/js/dataTables.bootstrap.min.js"></script>'
        print '<script src="lib/datatables.js"></script>'

        print '<script src="lib/iCheck/icheck.min.js"></script>'
        print "</body>"
        print "</html>"

    def redirect(self, path="index.py"):
        redirectURL = path
        print 'Content-Type: text/html'
        print 'Location: %s' % redirectURL
        print  # HTTP says you have to have a blank line between headers and content
        print '<html>'
        print '  <head>'
        print '    <meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
        print '    <title>You are going to be redirected</title>'
        print '  </head>'
        print '  <body>'
        print '    Redirecting... <a href="%s">Click here if you are not redirected</a>' % redirectURL
        print '  </body>'
        print '</html>'
