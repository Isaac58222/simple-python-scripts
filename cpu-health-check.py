#################################################################
# it may give error psutil model not found if it is not installed 
#
#################################################################
#!/bin/bash/env python3
import psutil
def check_cpu_usage(percent):
  usage = psutil.cpu_percent()
  return usage < percent
if not check_cpu_usage(75):
  print('ERROR! CPU overloaded')
else:
  print('everything ok')
