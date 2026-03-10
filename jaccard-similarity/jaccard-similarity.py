def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    if set_a == [] and set_b == []:
        return 0.0
    set1 = set(set_a)
    set2 = set(set_b)
    un_s= set1 | set2
    in_s=  set2 & set1

    if un_s == 0:
            return null

    return abs(len(in_s)) / abs(len(un_s))