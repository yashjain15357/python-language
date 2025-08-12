from pypdf import PdfWriter
a = PdfWriter()
b = PdfWriter()
# import os
# .write :- delete all the pages then write new things
# files = [file for file in os.listdir() if file.endswith(".pdf")]
for pdf in ["yash3.pdf", "yash3.pdf"]:
    a.append(pdf)                   # the pdf append in the 'a'
a.write("yash.3.pdf")                 # delete all the pages then write 'a' in the 'yash.pdf'

# b.append("yash.pdf", (0, 20))       # append 10 pages in the 'a' from the 'yash.pdf'
# b.write("yash1.pdf")                # delete all the pages then write 'a' in the 'yash1.pdf'

# a.append("yash.pdf",  [0, 9,1])     # append  0, 9,1 pages in the 'a' from the 'yash.pdf'
# a.write("yash.pdf")



# a.merge(position=2, fileobj="unit 5th.pdf", pages=(0, 5))
# a.write("yash.pdf")