import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

path = "E:\WebVision\Dataset\google\q0001"

file = open("data.txt", "r")
lines = file.readlines()
score = []
for line in lines:
	score.append(float(line))

# sorted_score = sorted(score)
# # print(sorted_score)
# # plt.hist(np.array(sorted_score), len(sorted_score))
# plt.plot(range(len(sorted_score)), sorted_score)
# plt.xlabel("Number")
# plt.ylabel("Score")
# plt.title("The score distribution of Google/q0001")
# plt.show()

files = os.listdir(path)
file_list = []
for file in files:
	file_path = os.path.join(path, file)
	if not os.path.isdir(file_path):
		file_list.append(file_path)

dict = {}
for i in range(len(file_list)):
	dict[file_list[i]] = score[i]
sorted_dict = sorted(dict.items(), key=lambda item:item[1])
# print(sorted_dict)

line_num = 6
fig_num = int(len(sorted_dict) / line_num**2 + 1)


with PdfPages('Scores.pdf') as pdf:
	for i in range(fig_num):
		fig = plt.figure(figsize = (12, 8), dpi = 100)
		
		for j in range(i * line_num**2, min((i+1) * line_num**2, len(sorted_dict))):
			plt.subplot(line_num, line_num, j%(line_num**2)+1)
			img = mpimg.imread(sorted_dict[j][0])
			plt.title(str(sorted_dict[j][1]))
			plt.imshow(img)
			plt.axis("off")
			plt.tight_layout()
		pdf.savefig(fig)
		plt.close()

# for i in range(len(sorted_dict)):
# 	fig_index = int(i / (line_num**2))
# 	plt.figure(fig_index)
# 	plt.subplot(line_num, line_num, i%(line_num**2)+1)
# 	img = mpimg.imread(sorted_dict[i][0])
# 	plt.title(str(sorted_dict[i][1]))
# 	plt.imshow(img)
# 	plt.axis("off")

# plt.show()