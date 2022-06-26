import shutil, os, glob, random

# List all files in a directory using os.listdir
basepath = 'small_data/source'
train_path = 'small_data/train_data'
test_path = 'small_data/test_data'
filenames = []
xmlnames = []

os.chdir('..')
print(os.getcwd())
for entry in os.listdir(basepath):
    file = os.path.join(basepath, entry)
    if os.path.isfile(file):
        if os.path.splitext(file)[1] == '.jpg':
            filenames.append(file)
        elif os.path.splitext(file)[1] == '.xml':
            xmlnames.append(file)
        else:
            continue

assert(len(filenames) == len(xmlnames))
indices = [i for i in range(len(filenames))]
filenames.sort()
xmlnames.sort()  # make sure that the filenames have a fixed order before shuffling
random.seed(230)
random.shuffle(indices)  # shuffles the ordering of filenames (deterministic given the chosen seed)

split = int(0.8 * len(filenames))
for idx in indices[:split]:
    shutil.copy(filenames[idx], train_path)
    shutil.copy(xmlnames[idx], train_path)

for idx in indices[split:]:
    shutil.copy(filenames[idx], test_path)
    shutil.copy(xmlnames[idx], test_path)
