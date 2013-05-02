import json
from operator import attrgetter

with open('teks.json', 'rb') as f:
  json_data = json.load(f)
f.closed

def makeSort(list_of_classes):
  return sorted(list_of_classes, key=attrgetter('title'))

class teksTop():
  def __init__(self, data):
    chapters = []
    for chapter in data:      
      chapters.append(teksChapter(data[chapter], chapter))
    self.chapters = makeSort(chapters)

class teksChapter():
  def __init__(self, data, key):
    subchapters = []
    self.title = data[0]
    self.id = key
    for subchapter in data[1]:
      subchapters.append(teksSubchapter(data[1][subchapter], subchapter))
    self.subchapters = makeSort(subchapters)

class teksSubchapter():
  def __init__(self, data, key):
    sections = []
    self.title = data[0]
    self.id = key
    for section in data[1]:
      sections.append(teksSections(data[1][section], section))
    self.sections = makeSort(sections)

class teksSections():
  def __init__(self, data, key):
    subsections = []
    self.title = data[0]
    self.id = key


teks = teksTop(json_data)
