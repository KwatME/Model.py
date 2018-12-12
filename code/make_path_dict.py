from ccal import establish_path


def make_path_dict(nmf_k, w_hcc_k, h_hcc_k, plotly_directory_name, upload_to_plotly):

    path_dict = {}

    name = "feature_x_sample.processed.tsv"

    path_dict[name] = "../output/{}".format(name)

    for name in ("feature_x_fit_parameter.tsv", "sample_x_fit_parameter.tsv"):

        path_dict[name] = "../output/fit/{}".format(name)

    for name in (
        "feature_x_sample.feature_context.tsv",
        "feature_x_sample.sample_context.tsv",
    ):

        path_dict[name] = "../output/context/{}".format(name)

    for name in (
        "feature_x_sample.raw_signal.tsv",
        "feature_x_sample.context_signal.tsv",
        "nmf/",
    ):

        path_dict[name] = "../output/signal/{}".format(name)

    for w_or_h in ("w", "h"):

        for name in ("{}.tsv".format(w_or_h), "{}/".format(w_or_h)):

            path_dict[name] = "../output/signal/nmf/{}/{}".format(nmf_k, name)

        for name in ("signature", "match", "hcc"):

            path_dict[
                "{}|{}/".format(w_or_h, name)
            ] = "../output/signal/nmf/{}/{}/{}".format(nmf_k, w_or_h, name)

        path_dict[
            "{}|hcc__k_x_column.tsv".format(w_or_h)
        ] = "../output/signal/nmf/{}/{}/hcc/hcc__k_x_column.tsv".format(nmf_k, w_or_h)

        if w_or_h is "w":

            hcc_k = w_hcc_k

        elif w_or_h is "h":

            hcc_k = h_hcc_k

        name = "cluster_x_column.tsv"

        path_dict[
            "{}|{}".format(w_or_h, name)
        ] = "../output/signal/nmf/{}/{}/hcc/{}/{}".format(nmf_k, w_or_h, hcc_k, name)

        for name in ("match", "map", "comparison"):

            path_dict[
                "{}|hcc|{}/".format(w_or_h, name)
            ] = "../output/signal/nmf/{}/{}/hcc/{}/{}".format(
                nmf_k, w_or_h, hcc_k, name
            )

    name = "gps_map.pickle.gz"

    path_dict[name] = "../output/signal/nmf/{}/{}".format(nmf_k, name)

    name = "summary/"

    path_dict[name] = "../output/{}".format(name)

    for name, path in path_dict.items():

        if name.endswith("/"):

            path_type = "directory"

        elif any(name.endswith(suffix) for suffix in (".tsv", ".pickle.gz")):

            path_type = "file"

        else:

            raise ValueError(name)

        establish_path(path, path_type)

    if upload_to_plotly:

        path_dict["plotly/"] = "Cellular Context/{}".format(plotly_directory_name)

    else:

        path_dict["plotly/"] = None

    for w_or_h, element_type_title in (("w", "Feature"), ("h", "Sample")):

        if upload_to_plotly:

            path_dict[
                "plotly|{}_match/".format(w_or_h)
            ] = "Cellular Context/{}/{} Match".format(
                plotly_directory_name, element_type_title
            )

            path_dict[
                "plotly|{}_map/".format(w_or_h)
            ] = "Cellular Context/{}/{} Map".format(
                plotly_directory_name, element_type_title
            )

        else:

            path_dict["plotly|{}_match/".format(w_or_h)] = None

            path_dict["plotly|{}_map/".format(w_or_h)] = None

    return path_dict
