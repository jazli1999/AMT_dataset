import mydataset

labels = [60, 62, 64, 65, 67, 69]

for label in labels:
	mydataset.dataset_gen(str(label))
