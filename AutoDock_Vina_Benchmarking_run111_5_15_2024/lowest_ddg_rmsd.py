import os, sys

motif_rmsd_file = "/data/project/thymelab/running_Rosetta/ari_work/REU_shared_space/benchmark/runs/run74_11-28-2022/rmsd_out/best_ddg_rmsds.csv"
#motif_rmsd_file = "/data/project/thymelab/running_Rosetta/ari_work/REU_shared_space/benchmark/runs/run60_03-27-2022_testing/rmsd_out/best_ddg_rmsds.csv"
autodock_rmsd_file = "/data/project/thymelab/running_Rosetta/ari_work/REU_shared_space/AutoDock_Vina_Benchmarking_Exhaustiveness/rmsd_of_best_ddg.csv"

system_rmsd_dict = {}

#counts for rmsds per method
motif_0_1 = 0
motif_1_2 = 0
motif_2_5 = 0
motif_5up = 0

auto_0_1 = 0
auto_1_2 = 0
auto_2_5 = 0
auto_5up = 0

#go through motifs and get systems with rmds
motif_file = open(motif_rmsd_file, "r")
autodock_file = open(autodock_rmsd_file, "r")

for line in motif_file.readlines():
	if "system" in line:
		continue
	sys = line.split(",")[0]
	rmsd = line.split(",")[2].strip("\n")

	system_rmsd_dict[sys] = [rmsd]

	rmsd = float(rmsd)

	if rmsd < 1:
		motif_0_1 = motif_0_1 + 1
	if rmsd >= 1 and rmsd < 2:
		motif_1_2 = motif_1_2 + 1
	if rmsd >= 2 and rmsd < 5:
		motif_2_5 = motif_2_5 + 1
	if rmsd >= 5:
		motif_5up = motif_5up + 1
#add autodock data
for line in autodock_file.readlines():
	if "system" in line:
		continue
	sys = line.split(",")[0]
	rmsd = line.split(",")[1].strip("\n")

	if sys in system_rmsd_dict.keys():
		system_rmsd_dict[sys].append(rmsd)

		rmsd = float(rmsd)
		if rmsd < 1:
			auto_0_1 = auto_0_1 + 1
		if rmsd >= 1 and rmsd < 2:
			auto_1_2 = auto_1_2 + 1
		if rmsd >= 2 and rmsd < 5:
			auto_2_5 = auto_2_5 + 1
		if rmsd >= 5:
			auto_5up = auto_5up + 1

	else:
		system_rmsd_dict[sys] = ["",rmsd]

for key in system_rmsd_dict.keys():
	print(key, system_rmsd_dict[key])

print("motif", motif_0_1, motif_1_2, motif_2_5, motif_5up)
print("autodock", auto_0_1, auto_1_2, auto_2_5, auto_5up)
#make csv file to compare
out_file = open("best_ddg_rmsds_comparison.csv", "w")
out_file.write("system,motifs,autodock\n")
for key in system_rmsd_dict.keys():
	#only write if we have entries for both
	if len(system_rmsd_dict[key]) == 2:
		out_file.write(key + "," + system_rmsd_dict[key][0] + "," + system_rmsd_dict[key][1] + "\n")
