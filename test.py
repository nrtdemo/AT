#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src_script.template import template_AT
import cgitb

cgitb.enable()
t = template_AT()


t.print_header()
# t.print_menu()
print '''<input type="text" id="X45" idfill="9" for="X45" dvdvar="" scripttype="comfill" tabindex="" buttonid="" datachangeevent="" value="สค.หาดใหญ่ (โครงการ IP Core 100G Over DWDM)_หาดใหญ่" flag="005" style="height:18px;margin-top:1px" name="instance/oss.source" maxlength="" onfocus="hpsm.widgets.Combo.handleOnFocus(this, event);" onblur="hpsm.widgets.Combo.handleOnBlur(this, event);" onclick="handleOnClick(this, event);" onchange="handleOnChange(this, event);" onkeydown="" aria-required="true">'''
print '''<input type="text" id="X49" name="instance/oss.destination" dvdvar="" buttonid="" datatype="string" sctype="Text" tabindex="" style="height:18px;margin-top:1px;" maxlength="" onkeyup="
                  handleOnChange(this, event);
                " onfocus="handleOnFocus(this, event);" onblur="handleOnBlur(this, event); applyToSameControl(this);" onclick="handleOnClick(this, event);" onchange="handleOnChange(this, event);" value="Teleport ศรีราชา (โครงการ IP Core 100G Over DWDM)_ศรีราชา" scripttype="text">'''
print '''<textarea id="X53" rows="2" cols="30" buttonid="" dvdvar="instance/oss.address/oss.address" tabindex="" sctype="MultiText" style="height:65px;" name="instance/oss.address/oss.address" onfocus="handleOnFocus(this, event);" onblur="handleOnBlur(this, event); applyToSameControl(this);" onclick="handleOnClick(this, event);" onchange="handleOnChange(this, event);" maxlength="" onkeyup="
    lockFormOnValueChange(this);
  ">เลขที่  หมู่  สค.หาดใหญ่ (ห้อง IP core Network)  ซอย  ชั้น 4 ถนน  ตำบล/แขวง บางกระสอ อำเภอ/เขต หาดใหญ่ จังหวัด สงขลา </textarea>'''
print '''<input type="text" id="X34" name="instance/oss.bandwidth" dvdvar="" buttonid="" datatype="string" sctype="Text" tabindex="" style="height:18px;margin-top:1px;" maxlength="" onkeyup="
                  handleOnChange(this, event);
                " onfocus="handleOnFocus(this, event);" onblur="handleOnBlur(this, event); applyToSameControl(this);" onclick="handleOnClick(this, event);" onchange="handleOnChange(this, event);" value="100 Gbps" scripttype="text">'''
# t.print_close()

