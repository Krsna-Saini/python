with open(r"221 Mail-Merge-Project-Start\Mail Merge Project Start\Input\Names\invited_names.txt", mode="r") as namefile:
    content = namefile.read()
names = content.split("\n")  # Split by newline to get individual names

with open(r"221 Mail-Merge-Project-Start\Mail Merge Project Start\Input\Letters\starting_letter.txt", mode="r") as contentfile:
    mail_content = contentfile.read()

placeholder = "[name]"

# Creating new files with names replaced in the letter
for name in names:
    if name.strip():
        row_mail = mail_content.replace(placeholder, name)
        print(row_mail)  # Optional, just for checking the output
        with open(f"{name}.txt", mode="w") as newtxt:
            newtxt.write(row_mail)
