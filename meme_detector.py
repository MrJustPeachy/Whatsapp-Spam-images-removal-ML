import pandas as pd
import numpy as np
import imgur_downloader
import urllib.error

data = [['Bern.csv', 'bern/'], ['Bernie.csv', 'bernie/'],
        ['Gary_Johnson.csv', 'gary_johnson/'], ['Clinton.csv', 'clinton/'],
        ['Democrat.csv', 'democrat/'], ['Donald.csv', 'donald/'],
        ['Feel_the_Bern.csv', 'feel_the_bern/'],
        ['Forward_Together.csv', 'forward_together/'],
        ['Hillary.csv', 'hillary/'], ['imwithher.csv', 'imwither/'],
        ['Jill_Stein.csv', 'jill_stein/'], ['Kaine.csv', 'kaine/'],
        ['Pence.csv', 'pence/'], ['Republican.csv', 'republican/'],
        ['Trump.csv', 'trump/']]

image_counter = 0
for filename, filedir in data:

    try:
        df = pd.read_csv(filename, encoding="ISO-8859-1")
        image_counter = 0
        for index, row in df.iterrows():
            if image_counter > 250:
                break
            image_id = row['id']
            image_link = row['link']
            image_caption = row['caption']
            try:
                imgur_downloader.ImgurDownloader(image_link,
                                                 'images/' + filedir,
                                                 str(image_id)).save_images()
                image_counter += 1
                print(image_id, image_link, image_caption)
            except Exception:
                print("Exception occured", filename)
    except UnicodeDecodeError:
        print("Unicode error", filename)
