from myRegexModule import clean_html

html_file = open('html_file.html', 'r')
raw_html = html_file.read()

clean_text = clean_html(raw_html)
print(clean_text)




