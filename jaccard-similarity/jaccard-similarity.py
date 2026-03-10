def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    if not set_a and  not set_b:
        return 0.0
    set1 = set(set_a)
    set2 = set(set_b)
    un_s= set1 | set2
    in_s=  set2 & set1

    if not un_s: 
            return None
# len is always non negative
    return len(in_s) / len(un_s)