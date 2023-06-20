def prettify_graph(graph):
    """Modify the given graph according to Jimmy's requests:
    add a title,
    make the y-axis start at 0,
    label the y-axis,
    format the tick marks as dollar amounts using the "$" symbol)
    """
    graph.set_title("Results of 500 slot machine pulls")
    # Complete steps 2 and 3 here
    graph.set_ylim(bottom=0)
    graph.set_ylabel("Balance")
    ticks = graph.get_yticks()
    new_labels = ["${}".format(int(amt)) for amt in ticks]
    graph.set_yticklabels(new_labels)
