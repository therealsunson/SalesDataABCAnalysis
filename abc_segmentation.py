def ABC_segmentation(run_perc: float) -> str:
    """Classify running percentage into ABC categories.

    Parameters
    ----------
    run_perc : float
        Running percentage of cumulative cost.

    Returns
    -------
    str
        'A' for values up to 0.8, 'B' for values up to 0.95, otherwise 'C'.
    """
    if run_perc <= 0.8:
        return "A"
    if run_perc <= 0.95:
        return "B"
    return "C"
