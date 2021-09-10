### Paper Linker

Insert links to citations that point to its cooresponding reference item.

### Install
```shell
git clone https://github.com/ramdrop/PaperLinker
cd PaperLinker
pip install -r requirements.txt
```

### Usage
``` shell
python paper_linker.py --pdf_in='input.pdf' --pdf_out='output.pdf'

```

### Help
```shell
/$ python paper_linker.py -h
usage: paper_linker.py [-h] [--conference {CVPR,ECCV,ICCV,ICRA,IROS,default}] [--max_ref MAX_REF] [--pdf_in PDF_IN] [--pdf_out PDF_OUT]

optional arguments:
  -h, --help            show this help message and exit
  --conference {CVPR,ECCV,ICCV,ICRA,IROS,default}
                        define citation and reference index templates
  --max_ref MAX_REF     the max number ofreference entries
  --pdf_in PDF_IN       pdf file to add links
  --pdf_out PDF_OUT     output pdf file with added links
```


---
The MIT License (MIT)


    Copyright (c) <2021> <Kaiwen Cai>

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
    the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
    FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.