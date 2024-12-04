def print_report(file):
  text = read_book(file)
  sorted_list = sorted_dict_list(count_char_dict(text))
  print(f"--- Begin report of {file} ---")
  print(f"{count_words(text)} words found in the document")
  print()
  
  for dict in sorted_list:
    if dict["char"].isalpha():
      print(f"The '{dict["char"]}' character was found {dict["count"]} times")
  print("--- End report ---")

def sort_on(dict):
  return dict["count"]

def sorted_dict_list(dict):
  list = []
  for key in dict:
    list.append({"char": key, "count": dict[key]})
  list.sort(reverse=True, key=sort_on)
  return list

def count_char_dict(text):
  dict = {}
  lowered_text = text.lower()
  for char in lowered_text:
    if char in dict:
      dict[char] += 1
    else:
      dict[char] = 1
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