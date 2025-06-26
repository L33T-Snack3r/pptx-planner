import re

def find_text_in_between_tags(text, start_tag, end_tag):
    result = []
    start_pos = text.find(start_tag)
    end_pos = text.find(end_tag)
    while start_pos > -1 and end_pos > -1:
        text_between_tags = text[start_pos + len(start_tag):end_pos].strip()
        result.append(text_between_tags)
        start_pos = text.find(start_tag, end_pos + len(end_tag))
        end_pos = text.find(end_tag, start_pos)
    res1 = "".join(result).strip()
    res2 = re.sub(r"\[IMAGE\].*?\[/IMAGE\]", '', res1).strip()
    return res2 if len(result) > 0 else ""