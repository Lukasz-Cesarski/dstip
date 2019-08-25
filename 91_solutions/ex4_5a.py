def compare_releases(target_rel, comp_rels, df_kpi):
    target_df = df_kpi[target_rel]
    comp_df   = df_kpi[comp_rels]
    result = comp_df.apply(lambda x: x - target_df, axis=0)
    return result