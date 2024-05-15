import os,sys

location = os.getcwd()

system_rmsd_dict = {}

for r,d,f in os.walk(location):
        for file in f:
                if file.endswith("_ddg_vs_rmsd.csv"):
                        #get the first line of the file to get the rmsd for the system
                        read_file = open(r + "/" + file, "r")

                        rmsd = ""
                        for line in read_file.readlines():
                                rmsd = line.split(",")[1].strip("\n")
                                break

                        read_file.close()
                        system_rmsd_dict[file.split("_")[0]] = str(rmsd)

print(system_rmsd_dict, len(system_rmsd_dict))

#write to output file
write_file = open("rmsd_of_best_ddg.csv", "w")
write_file.write("system,rmsd\n")
for key in system_rmsd_dict.keys():
        write_file.write(key + "," + system_rmsd_dict[key] + "\n")

