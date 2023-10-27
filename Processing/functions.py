import os
import json
import tweepy
from pprint import pprint
from sklearn.feature_extraction.text import TfidfVectorizer
from datetime import datetime
from pprint import pprint
import pickle

root = r"pheme-rnr-dataset"
events = ['ottawashooting', 'germanwings-crash', 'charliehebdo', 'sydneysiege', 'ferguson']


def process_datetime(raw: str):
    date_format = "%a %b %d %H:%M:%S %z %Y"
    datetime_obj = datetime.strptime(raw, date_format)
    return int(round(datetime_obj.timestamp()))


def extract_information(tid: int, category):
    file = open(f"{root}/{event}/{category}/{tid}/source-tweet/{tid}.json")
    data = json.load(file)

    content = data['text']
    datetime = process_datetime(data['created_at'])

    return content, datetime


def extract_information_from_comment_file(source_tid, claim_file, category):
    file = open(f"{root}/{event}/{category}/{source_tid}/reactions/{claim_file}")
    data = json.load(file)

    content = data['text']
    datetime = process_datetime(data['created_at'])

    return content, datetime


