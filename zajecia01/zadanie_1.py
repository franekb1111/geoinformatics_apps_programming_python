import json

with open('teksty.json', 'r') as file:
 content = file.read()

content = content.lower()

js = json.loads(content)

# print(js)

#print(js["TEKSTY"])

combined_text = ""

for item in js["teksty"]:
    for text in item.values():
        combined_text += text 

#print(combined_text)

combined_text_b = combined_text.replace('.', '')
combined_text_b = combined_text_b.replace(',', '')

#print(combined_text_b)

words = combined_text_b.split()

for i in range(len(words)):
    last_letter = words[i][-1].upper()
    words[i] = words[i][:-1] + last_letter

combined_text_d = ' '.join(words)

filtered_words = [word for word in words if 'a' not in word and 'A' not in word]

combined_text_not = ' '.join(filtered_words)

#print(combined_text_not)


uniques = list(set(words))


word_count = {}

for word in words:
    count = words.count(word)
    word_count[word] = count

#print(word_count)

koncowy_json = {
   "duze_na_male" : combined_text,
   "wyrazy" : words,
   "bez_znakow_interpunk" : combined_text_b,
   "ostatnia_duza_litera" : combined_text_d,
   "wyrazy_bez_a_A" : combined_text_not,
   "unikatowe" : uniques,
   "liczba_wystapien" : word_count
}

koncowy_json = json.dumps(koncowy_json)

with open("zadanie_1.json", "w") as outfile:
    outfile.write(koncowy_json)