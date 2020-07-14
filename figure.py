import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-p1begin', type=str, default="", help="the begin time of p1")
parser.add_argument('-p2begin', type=str, default="", help="the begin time of p2")
parser.add_argument('-p1end', type=str, default="", help="the end time of p1")
parser.add_argument('-p2end', type=str, default="", help="the end time of p2")
parser.add_argument('-f', type=str, default="", help="the location of the csv file")
args = parser.parse_args()
file = args.f
p1begin = args.p1begin
p2begin = args.p2begin
p1end = args.p1end
p2end = args.p2end
# command1 = "python3 ~/monk/fcyDataAnalysis/monk.py --readFile "+file+" --writeFile ./figure/"
command1 = "python3 ./monk.py --readFile "+file+" --writeFile ./figure/"
command_time_p1 = "--begin '"+p1begin+"' --end '"+p1end+"' "
command_time_p2 = "--begin '"+p2begin+"' --end '"+p2end+"' "
item = "--item "
print("*******************************************************p1****************************")
print("p1_memory_used figure finished")
command_p1_memused = command1+"p1_mem_used.png "+command_time_p1+item+"used"
os.system(command_p1_memused)
print("p1_cpu_used figure finished")
command_p1_cpu = command1+"p1_cpu.png "+command_time_p1+item+"usr"
os.system(command_p1_cpu)
print("p1_read figure finished")
command_p1_read = command1+"p1_read.png "+command_time_p1+item+"read"
os.system(command_p1_read)
print("p1_write_figure finished")
command_p1_write = command1+"p1_write.png "+command_time_p1+item+"writ"
os.system(command_p1_write)
print("p1_in_figure finished")
command_p1_in = command1+"p1_in.png "+command_time_p1+item+"in"
os.system(command_p1_in)
print("p1_out figure finished")
command_p1_out = command1+"p1_out.png "+command_time_p1+item+"out"
os.system(command_p1_out)


print("******************************************************p2****************************")
print("p2_memory_used figure finished")
command_p2_memused = command1+"p2_mem_used.png "+command_time_p2+item+"used"
os.system(command_p2_memused)
print("p2_cpu_used figure finished")
command_p2_cpu = command1+"p2_cpu.png "+command_time_p2+item+"usr"
os.system(command_p2_cpu)
print("p2_read figure finished")
command_p2_read = command1+"p2_read.png "+command_time_p2+item+"read"
os.system(command_p2_read)
print("p2_write_figure finished")
command_p2_write = command1+"p2_write.png "+command_time_p2+item+"writ"
os.system(command_p2_write)
print("p2_in_figure finished")
command_p2_in = command1+"p2_in.png "+command_time_p2+item+"in"
os.system(command_p2_in)
print("p2_out figure finished")
command_p2_out = command1+"p2_out.png "+command_time_p2+item+"out"
os.system(command_p2_out)
