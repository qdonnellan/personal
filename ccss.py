import json
from operator import attrgetter

with open('ccss.json', 'rb') as f:
  json_data = json.load(f)
f.closed

namemap = {
      '1' : 'Grade 1',
      '2' : 'Grade 2', 
      '3' : 'Grade 3', 
      '4' : 'Grade 4',
      '5' : 'Grade 5', 
      '6' : 'Grade 6', 
      '7' : 'Grade 7',
      '8' : 'Grade 8', 
      '6-8' : 'Grades 6-8', 
      '9-10' : 'Grades 9-10',
      '11-12' : 'Grades 11-12', 
      'K' : 'Kindergarten', 
      'RH' : 'History/Social Studies',
      'RST' : 'Science & Technical Subjects',
      'Practice' : 'Mathematical Practice',
      'HSN' : 'High School: Number and Quantity',
      'HSA' : 'High School: Algebra',
      'HSF' : 'High School: Functions',
      'HSG' : 'High School: Geometry',
      'HSS' : 'High School: Statistics & Probability',
      'CCRA' : 'College and Career Readiness Anchor Standards (CCRAS)',
      'RL' : 'Reading: Literature',
      'RI' : 'Reading: Informational Text',
      'RF' : 'Reading: Foundational Skills', 
      'W' : 'Writing',
      'SL' : 'Speaking & Listening',
      'L' : 'Language',
      'R' : 'Reading',
      'WHST' : 'Writing for History/Social Studies, Science, & Technical Subjects',
      'CCRA-R' : 'Anchor Standards for Reading',
      'CCRA-W' : 'Anchor Standards for Writing',
      'CCRA-SL' : 'Anchor Standards for Speaking & Listening',
      'CCRA-L' : 'Anchor Standards for Language',
    }

def mapKey(key):
  if key in namemap:
    return namemap[key]
  else:
    return key

def makeSort(list_of_classes):
  return sorted(list_of_classes, key=attrgetter('title'))

class ccssTop():
  def __init__(self, data):
    domains = []
    for domain in data:
      domains.append(ccssDomain(data[domain], domain))
    self.domains = makeSort(domains)

class ccssDomain():
  def __init__(self,data, key):
    subdomains = []
    self.title = key
    self.id = key
    for subdomain in data:
      subdomains.append(ccssSubDomain(data[subdomain], subdomain))
    self.subdomains = makeSort(subdomains)

class ccssSubDomain():
  def __init__(self,data, key):
    strands = []
    self.title = mapKey(key)
    self.id = key
    for strand in data:
      strands.append(ccssStrand(data[strand], strand, self.title))
    self.strands = makeSort(strands)

class ccssStrand():
  def __init__(self,data,key, subdomain_title):
    if 'CCRA' in subdomain_title:  
      self.title = mapKey('CCRA-'+ key)
    else:
      self.title = mapKey(key)
    self.id = key

ccss = ccssTop(json_data)



