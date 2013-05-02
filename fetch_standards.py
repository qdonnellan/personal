from teks import teks
import ccss
import re

def splitQuery(query_string):
  standards = query_string.split('|')
  nonblank_standards = []
  for standard in standards:
    if standard not in ['', None]:
      nonblank_standards.append(standard)
  return nonblank_standards

def fetchTEKS(teks_string):
  standard = re.sub('teks-', '', teks_string)
  for chapter in teks.chapters:
    for subchapter in chapter.subchapters:
      for section in subchapter.sections:
        if standard == section.id:
          standard = ['(TEKS)', section.title]
  return standard

def fetchCCSS(ccss_string):
  standard_levels = ccss_string.split('.')
  ccss_standard = ['(CCSS)']
  for level in standard_levels:
    if level in ccss.namemap:     
      ccss_standard.append(ccss.namemap[level])
    else:
      ccss_standard.append(level)
  return ccss_standard

def fetch(query_string):
  these_standards = []
  for standard in splitQuery(query_string):
    if 'teks' in standard:
      standard = fetchTEKS(standard)
    else:
      standard = fetchCCSS(standard)

    these_standards.append(standard)
  return these_standards




