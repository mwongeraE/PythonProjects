def anti_vowel(text):
  vowels = 'aeiou'
  newtext = ''
  for i in text:
    if i.lower() not in vowels:
      newtext += i
  return newtext
