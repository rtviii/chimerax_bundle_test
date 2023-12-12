
def fetch_ribxz_profile(session, rcsb_id, ignore_cache=True, **kw):

    """Fetch and display sequence alignment for 'ident' from HomoloGene.
    Use Python library to download the FASTA file and use ChimeraX
    alignment tools for display.
    """

    # First fetch the file using ChimeraX core function

    url =  "http://127.0.0.1:8000/comp/get_profile/?rcsb_id={}".format(rcsb_id)
    session.logger.status("Fetching ribxz %s" % rcsb_id)
    save_name = "%s_profile.json" % rcsb_id

    from chimerax.core.fetch import fetch_file
    filename = fetch_file(session, url, "ribxz %s" % rcsb_id, save_name, "HomoloGene", ignore_cache=ignore_cache, uncompress=True)
    session.logger.status("Opening ribxz %s" % rcsb_id)
    models, status = session.open_command.open_data(filename, alignment=False, name=rcsb_id)

    return models, status