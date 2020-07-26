import heapq


def nlargest(n, dicts_list, key):
    def _sort_key(dict_element):
        return dict_element[key]

    return heapq.nlargest(n, dicts_list, _sort_key)
