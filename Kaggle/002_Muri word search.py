def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword
    {'casino': [0, 1], 'they': [1]}
    """

    def word_search(doc_list, keyword):
        """
        Takes a list of documents (each document is a string) and a keyword.
        Returns list of the index values into the original list for all documents
        containing the keyword.

        Example:
        doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"
        """
        indices = []
        for i, doc in enumerate(doc_list):
            tokens = doc.split()
            normalized = [token.rstrip('.,').lower() for token in tokens]
            if keyword.lower() in normalized:
                indices.append(i)
        return indices

    kw_dict = {}
    for kw in keywords:
        kw_dict[kw] = word_search(doc_list, kw)
    return kw_dict