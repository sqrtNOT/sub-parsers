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


def parseass(path):
    import re
    document = open(path, 'r').read()
    arr = []
    header = re.compile(r"\[Events\]\s*?\nFormat:\s*([\s\S]+?)\n").findall(document)[0].lower().split(',')
    for i, field in zip(range(len(header)), header):
        header[i] = field.strip()
    data = re.compile(r"\nDialogue:([\s\S]+?)(?=\nDialogue:|\Z)").findall(document)
    for datum in data:
        tokens = datum.split(',')
        for i, token in zip(range(len(tokens)), tokens):
            tokens[i] = token.strip()
        dic = {k: v for (k, v) in zip(header, tokens)}
        arr.append(dic)
    return arr
