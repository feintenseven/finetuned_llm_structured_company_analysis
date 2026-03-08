def text_to_list(sectionsall):
    tot=[]
    sectionsin=sectionsall.strip().split('\n\n\n')
    for sections in sectionsin:
        lst=[]
        sections=sections.strip().split('\n\n')
        for section in sections:
            g=section.split('\n')
            currlst=[]
            for k in g[1:]:
                currlst.append(k)
            lst.append(currlst)
        tot.append(lst)
    return tot