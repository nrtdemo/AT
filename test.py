#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src_script.template import template_AT
import cgitb

cgitb.enable()
t = template_AT()


t.print_header()
t.print_menu()
print '<input type="text" id="X45" idfill="9" for="X45" dvdvar="" scripttype="comfill" tabindex="" buttonid="" datachangeevent="" value="กสท คลองหลวง_คลองหลวง" flag="005" style="height:18px;margin-top:1px" name="instance/oss.source" maxlength="" onfocus="hpsm.widgets.Combo.handleOnFocus(this, event);" onblur="hpsm.widgets.Combo.handleOnBlur(this, event);" onclick="handleOnClick(this, event);" onchange="handleOnChange(this, event);" onkeydown="" aria-required="true">'
t.print_close()

