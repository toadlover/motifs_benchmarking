import os, sys

location = os.getcwd()

#loop through all directories at location, want to look at the rmsd.txt in any directories to collect the rmsds in model order. Then look at the output.pdbqt and get the corresponding ddg. Group the values together and put into a csv file for graphical analysis

for r,d,f in os.walk(location):
	for directory in d:
		#if output.pdbqt and rmsd.txt exist in the directory
		if os.path.isfile(r + "/" + directory + "/output.pdbqt") and os.path.isfile(r + "/" + directory + "/rmsd.txt"):
			
			print("files exist for " + directory)

			#read output.pdbqt and make a list of energies
			file_energies = []

			placement_file = open(r + "/" + directory + "/output.pdbqt", "r")
			for line in placement_file.readlines():
				#ddg located on line that starts with "REMARK VINA RESULT", ddg is at split index 3
				if line.startswith("REMARK VINA RESULT"):
					file_energies.append(line.split()[3])

			placement_file.close()

			#read rmsd file and get rmsds out
			rmsds = []
			rmsd_file = open(r + "/" + directory + "/rmsd.txt", "r")
			for line in rmsd_file.readlines():
				#ignore the first line that holds the best rmsd. remaining are in order
				if line.startswith("Best"):
					continue
				rmsds.append(line.strip("\n"))
			rmsd_file.close()

			#order of both lists should be the same
			#output to ddg_vs_rmsd.csv file
			#output ddg then rmsd

			out_file = open(r + "/" + directory + "/" + directory + "_ddg_vs_rmsd.csv", "w")
			for i in range(len(file_energies)):
				out_file.write(str(file_energies[i]) + "," + str(rmsds[i]) + "\n")
			out_file.close()
