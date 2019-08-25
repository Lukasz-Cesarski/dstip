def compare_tests(target_rel, comp_rels, df_tests):
    # comp_df = df_tests[df_tests['release'].apply(lambda x: x in comp_rels)] # using mask
    comp_df = df_tests.query("release in @comp_rels") # using query
    # target_df = df_tests[df_tests['release'] == target_rel] # using mask
    target_df = df_tests.query("release == @target_rel") # using query
    join_cols = ["language"]
    result = comp_df.join(target_df.set_index(join_cols), on=join_cols, lsuffix = "_base", rsuffix="_target")
    result["difference"] = result["kpi_base"] - result["kpi_target"]
    return result