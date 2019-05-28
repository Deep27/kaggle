from nolearn.dbn import DBN
import csv
import numpy as np

net = DBN(
    [784, 300, 10],
    learn_rates=0.3,
    learn_rate_decays=0.9,
    epochs=10,
    verbose=1
)

with open('./data/train.csv', 'rb') as f:
    data = list(csv.reader(f))

train_data = np.array(data[1:])
labels = train_data[:, 0].astype('float')
train_data = train_data[:, 1:].astype('float') / 255.0

net.fit(train_data, labels)

with open('./data/test.csv', 'rb') as f:
    data = list(csv.reader(f))

test_data = np.array(data[1:]).astype('float') / 255.0
preds = net.predict(test_data)

with open('./data/submission.csv', 'wb') as f:
    writer = csv.DictWriter(f, fieldnames=['ImageId', 'Label'])
    writer.writeheader()
    i = 1
    for e in preds:
        writer.writerow({'ImageId': i, 'Label': e})
        i += 1
