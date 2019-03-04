import json
from sklearn.model_selection import train_test_split

def create_gt(data_folder, test_size, val_size, random_state):

    maxTextLen = 30

    #filenames = []
    #labels = []

    dataset = []
    
    f=open(data_folder + 'words.txt')
    chars = set()
    for line in f:
        # ignore comment line
        if not line or line[0]=='#':
            continue

        line_split = line.strip().split(' ')
        assert len(line_split) >= 9

        # filename: part1-part2-part3 --> part1/part1-part2/part1-part2-part3.png
        filename_split = line_split[0].split('-')
        filename = data_folder + 'words/' + filename_split[0] + '/' + filename_split[0] + '-' + filename_split[1] + '/' + line_split[0] + '.png'

        # GT text are columns starting at 9
        label = ' '.join(line_split[8:])[:maxTextLen]
        chars = chars.union(set(list(label)))

        #filenames.append(filename)
        #labels.append(label)

        # put sample into list
        dataset.append((filename, label))

    #split in train val test
#    filenames_train_val, filenames_test, labels_train_val, labels_test = train_test_split(filenames, labels, test_size=test_size, random_state=random_state)  
#    filenames_train, filenames_val, labels_train, labels_val = train_test_split(filenames_train_val, labels_train_val, test_size=val_size, random_state=random_state)      

    dataset_train_val, dataset_test = train_test_split(dataset, test_size=test_size, random_state=random_state)  
    dataset_train, dataset_val = train_test_split(dataset_train_val, test_size=val_size, random_state=random_state)      

    dataset_out = {}

    dataset_out['train'] = dataset_train
    dataset_out['val'] = dataset_val
    dataset_out['test'] = dataset_test
    
    return dictionary

if __name__ == '__main__':

    data_folder = '../datasets/'
    filename_out = 'gt.json'
    
    dataset_out = create_gt(data_folder,  test_size = 0.1, val_size = 0.1, random_state = 46)
    
    with open(data_folder + filename_out, 'w') as f:
        json.dump(dataset_out, f)
    