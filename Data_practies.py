word={"one":"один","two": "два", "three":"три", "four":"четыре", "fife":"пять"}
for stroka in open("data.txt"):
  str_mas=stroka.split()
  for el in str_mas:
    for key,val in word.items():
      if el.lower()==key:
        el=val+" "
  file2=open("dataRu.txt","a")
  file2.writelines(str_mas)

file2.read()
file2.close()