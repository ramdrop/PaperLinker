# %%
# PyMuPDF https://pymupdf.readthedocs.io/en/latest/index.html
import fitz
# PyPDF2 https://pythonhosted.org/PyPDF2/index.html
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import RectangleObject

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--conference",
                    type=str,
                    default='default',
                    choices=['CVPR', 'ECCV', 'ICCV', 'ICRA', 'IROS', 'default'],
                    help='define citation and reference index templates')
parser.add_argument("--max_ref", type=int, default=50, help='the max number ofreference entries')
parser.add_argument("--pdf_in", type=str, default='', help='pdf file to add links')
parser.add_argument("--pdf_out", type=str, default='', help='output pdf file with added links')
args = parser.parse_args()

# define cite and reference templates
src_templates = ["[{}]", "[{}", "{}]"]
refer_template = '{}. '

if args.conference == 'ECCV':
    refer_template = '{}. '
    src_templates = ["[{}]", "[{}", "{}]"]
elif args.conference == 'CVPR':
    refer_template = '[{}]'
    src_templates = ["[{}]", "[{}", "{},", "{}]"]
elif args.conference == 'ICRA':
    refer_template = '[{}]'
    src_templates = ["[{}]", "[{}", "{},", "{}]"]

doc = fitz.open(args.pdf_in)
page_count = doc.pageCount
for page in doc:
    dict_ = page.getText('dict')
    W_f, H_f = dict_["width"], dict_["height"]
    text_instances = page.searchFor("REFERENCES")
    if text_instances != []:
        reference_page_num = page.number
        break

dst_dict = dict()
for cite_index in range(1, args.max_ref):                            # within max reference entries
    for page_index in range(reference_page_num, page_count):         # search references only in reference pages
        page = doc.loadPage(page_index)
        src_txt = refer_template.format(cite_index)
        text_instances = page.searchFor(src_txt)
        if text_instances != []:
            dst_dict[cite_index] = page.number
            break
reference_total_num = list(dst_dict.keys())[-1]

link_queue = []
for page_index in range(0, reference_page_num):            # search citations only in body pages
    page = doc.loadPage(page_index)
    for template in src_templates:
        for cite_index in range(1, reference_total_num + 1):
            src_txt = template.format(cite_index)
            text_instances = page.searchFor(src_txt)
            if text_instances != []:
                src_pagenum = page.number
                for item in text_instances:
                    bl_x, ur_y, ur_x, bl_y = item.irect
                    link_queue.append(
                        [src_pagenum, reference_page_num if args.conference == 'default' else dst_dict[cite_index], bl_x, ur_y, ur_x, bl_y])


print('{} links to add..'.format(len(link_queue)))

# %%
# open the pdf file
pdf_reader = PdfFileReader(args.pdf_in)
pdf_writer = PdfFileWriter()

# get number of pages
NumPages = pdf_reader.getNumPages()

for page_index in range(NumPages):
    page = pdf_reader.getPage(page_index)
    pdf_writer.addPage(page)
    _, _, W, H = page.mediaBox
    assert W - W_f < 1 and H - H_f < 1, 'size parsing error!'

# link_queue.append([src_pagenum, dst_pagenum, bl_x, ur_y, ur_x, bl_y])
for item in link_queue:
    bl_x, bl_y, ur_x, ur_y = item[2], H - item[5], item[4], H - item[3]
    pdf_writer.addLink(pagenum=item[0], pagedest=item[1], rect=RectangleObject([bl_x, bl_y, ur_x, ur_y]), border="dott", fit='/Fit')

pdf_out = args.pdf_out if args.pdf_out != '' else args.pdf_in
with open(pdf_out, 'wb') as fh:
    pdf_writer.write(fh)

print('{} ==> {}'.format(args.pdf_in, pdf_out))
