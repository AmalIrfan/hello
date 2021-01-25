'''
                         ,,    ,,                                                    ,,     ,,      
`7MMF'  `7MMF'         `7MM  `7MM                          db                        db     db    OO
  MM      MM             MM    MM                         ;MM:                                    88
  MM      MM   .gP"Ya    MM    MM   ,pW"Wq.              ,V^MM.    ,pP"Ybd  ,p6"bo `7MM   `7MM    ||
  MMmmmmmmMM  ,M'   Yb   MM    MM  6W'   `Wb            ,M  `MM    8I   `" 6M'  OO   MM     MM    ||
  MM      MM  8M""""""   MM    MM  8M     M8            AbmmmqMA   `YMMMa. 8M        MM     MM    `'
  MM      MM  YM.    ,   MM    MM  YA.   ,A9  ,,       A'     VML  L.   I8 YM.    ,  MM     MM    ,,
.JMML.  .JMML. `Mbmmd' .JMML..JMML. `Ybmd9'   dg     .AMA.   .AMMA.M9mmmP'  YMbmd' .JMML. .JMML.  db
                                              ,j                                                    
                                             ,'             Font: georgia11 from art module     
'''

from sys import stdout
from time import sleep
from random import randint
import textwrap

# Config
speed_range = 0,1 # ms

# Each Letters of our word
# There might be a better way but I like being able to tweek
Letters = [
'''
`7MMF'  `7MMF'
  MM      MM
  MM      MM
  MMmmmmmmMM
  MM      MM
  MM      MM
.JMML.  .JMML.

''',
'''


 .gP"Ya 
,M'   Yb
8M""""""
YM.    ,
 `Mbmmd' 

''',
'''\
  ,,
`7MM
  MM
  MM
  MM
  MM
  MM
.JMML.

''',
'''\
  ,,
`7MM
  MM
  MM
  MM
  MM
  MM
.JMML.

''',
'''


 ,pW"Wq.
6W'   `Wb
8M     M8
YA.   ,A9
 `Ybmd9'

''',
'''





 ,,
 dg
 ,j
,'     \
''',
'''
      db
     ;MM:
    ,V^MM.
   ,M  `MM
   AbmmmqMA
  A'     VML
.AMA.   .AMMA.
''',
'''


,pP"Ybd
8I   `"
`YMMMa.
L.   I8
M9mmmP'
''',
'''


 ,p6"bo
6M'  OO
8M
YM.    ,
 YMbmd' 
''',
'''\
  ,,
  db

`7MM
  MM
  MM
  MM
.JMML. 
''',
'''\
  ,,
  db

`7MM
  MM
  MM
  MM
.JMML.  
''',
'''
OO
88
||
||
`'
,,
db
'''
]


lastH = 0
lastV = 0
ESC = 0

try:
    stdout.write("\033[?25l")
    for string in Letters:
        ostr = iter(textwrap.indent(string,"\[\033[C"*lastH+"\]"))
        for c in ostr:
            if c == "\\":
                c += next(ostr,"")
            if c.endswith("\["):
                ESC = 1
                continue
            if c.endswith("\]"):
                ESC = 0
                continue
            stdout.write(c)
            if not ESC:
                stdout.flush()
                sleep(randint(*speed_range)*.001)

        lastV = string.count("\n")
        stdout.write("\033[A"*lastV)
        stdout.flush()
        lastH += len(max(string.splitlines(1),key=lambda x: len(x.replace("\n",""))))
finally:
    stdout.write("\033[?25h")
    stdout.write("\033[B"*lastV+"\n")