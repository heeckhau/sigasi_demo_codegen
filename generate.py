#!/usr/bin/python
import sys, re, time

registers = [
  ("foo",0x0000cafe),
  ("bar",0x00facade)
  ]

def interp(string):
  locals  = sys._getframe(1).f_locals
  globals = sys._getframe(1).f_globals
  for item in re.findall(r'#\{([^{]*)\}', string):
    string = string.replace('#{%s}' % item,
                            str(eval(item, globals, locals)))
  return string
  
def to_vhdl_constant(register):
	address = register[1]
	hex_address = "%08x"%address
	name = register[0]
	return interp('constant #{name}_address : integer := 16##{hex_address}#;')
	
vhdl_constants = [to_vhdl_constant(register) for register in registers]

vhdl_constants_string = reduce(lambda x,y : x+"\n"+y, vhdl_constants, "")[1:]

package_skeleton="""-- file generated at #{datestamp}
package p is
#{declaration_part}
end package p;
"""

datestamp = time.asctime( time.localtime(time.time()) )
declaration_part = vhdl_constants_string
package_declaration = interp(package_skeleton) 

f = open("package.vhd", "w")
f.write(package_declaration);
f.close
