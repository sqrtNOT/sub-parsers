def parsesrt(path):
    import re
    document = open(path, 'r').read()
    results = re.compile(r"""
        (\d+)\s*?\n  # line number
        (\d+:\d+:\d+,\d+)\s*?-->\s*?(\d+:\d+:\d+,\d+) # start --> end
        ([\s\S]+?)  # subtitle text
        (?=\n\d+\n+\d+:\d+:\d+,\d+\s*?-->|\Z) # stop at next subtitle or end of document
        """, re.VERBOSE).findall(document)
    arr = []
    for tup in results:
        _dic = {"line": tup[0], "start": tup[1], "end": tup[2], "text": tup[3].strip()}
        arr.append(_dic)
    return arr
