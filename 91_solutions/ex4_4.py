water_part = df_density['Water_km2']/df_density['Total_km2']
display(water_part.sort_values(ascending=False).index[:5].tolist())