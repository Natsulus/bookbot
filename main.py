def print_report(file):
  text = read_book(file)
  list = sorted_dict_list(count_char_dict(text))
  print(f"--- Begin report of {file} ---")
  print(f"{count_words(text)} words found in the document")
  print()
  
  for char in list:
    if char["char"].isalpha():
      print(f"The '{char["char"]}' character was found {char["count"]} times")
  print("--- End report ---")
  return

def sort_on(dict):
  return dict["count"]

def sorted_dict_list(dict):
  sorted = []
  for char in dict:
    sorted.append({"char": char, "count": dict[char]})
  sorted.sort(reverse=True, key=sort_on)
  return sorted

def count_char_dict(text):
  dict = {}
  lowered_text = text.lower()
  for c in lowered_text:
    if c in dict:
      dict[c] += 1
    else:
      dict[c] = 1
  return dict

def count_words(text):
  words = text.split()
  return len(words)

def read_book(file):
  with open(file) as f:
    return f.read()

def main():
 print_report("books/frankenstein.txt")

main()