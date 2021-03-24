import csv
from textblob import TextBlob 

def read_data(file_name):
    file_name_to_read = file_name
    f = open(file_name_to_read,'r',encoding='utf-8')
    csv_reader = csv.reader(f)
    list_of_row = []
    for row in csv_reader:
        list_of_row.append(row)
    return(list_of_row[1:]) # change to [1:] if want to have every rows

data = read_data("Review.csv") # type your name of the file
data_length = len(data)

data_polarity = []
for i in range(data_length):
    text = TextBlob(data[i][1])

    if text.sentiment.polarity > 0 and text.sentiment.polarity <= 1:
        data_polarity.append([data[i][0],'Positive'])
    elif text.sentiment.polarity == 1:
        data_polarity.append([data[i][0], 'Netural'])
    else:
        data_polarity.append([data[i][0], 'Negative'])

# print(data_polarity)
    
f = open('yelp_sent_result.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(['review_id','Polarity(Neg/Pos/Neu)'])
for i in range(data_length):
    wr.writerow(data_polarity[i])
f.close()