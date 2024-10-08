import pandas as pd

# Function to calculate compound annual growth rate (CAGR)
def calculate_cagr(start_population, end_population, years):
    return ((end_population / start_population) ** (1 / years) - 1) * 100  # Return as a percentage

# Example population data for counties
population_data = {
# Re-creating the population data for all counties and adding missing Florida data
        'Alachua': [271588, 283035, 292692, 300261, 306332, 311324],
        'Baker': [28532, 29882, 31017, 31957, 32728, 33387],
        'Bay': [174410, 185038, 193082, 199010, 203693, 207593],
        'Bradford': [28725, 29260, 29650, 29930, 30190, 30441],
        'Brevard': [606671, 643112, 671329, 694250, 714874, 733563],
        'Broward': [1932212, 2013797, 2083767, 2142335, 2192705, 2237840],
        'Calhoun': [14489, 15120, 15598, 15950, 16228, 16460],
        'Charlotte': [187904, 203016, 215478, 225562, 234391, 242460],
        'Citrus': [149383, 156569, 162381, 166880, 170762, 174329],
        'Clay': [219575, 237339, 252446, 264550, 274802, 283855],
        'Collier': [387450, 423564, 452806, 477771, 499729, 518956],
        'Columbia': [70617, 73506, 75881, 77689, 79177, 80462],
        'DeSoto': [37082, 38730, 39959, 40941, 41754, 42469],
        'Dixie': [16663, 16956, 17166, 17313, 17424, 17528],
        'Duval': [982080, 1043160, 1092238, 1131522, 1164144, 1192525],
        'Escambia': [323714, 335093, 344048, 351239, 357680, 363494],
        'Flagler': [114173, 128283, 140758, 150941, 159426, 166907],
        'Franklin': [11864, 12384, 12778, 13068, 13297, 13488],
        'Gadsden': [46226, 46820, 47204, 47426, 47563, 47649],
        'Gilchrist': [18269, 19332, 20170, 20848, 21420, 21924],
        'Glades': [13609, 14272, 14811, 15222, 15560, 15851],
        'Gulf': [14724, 15399, 15909, 16286, 16583, 16831],
        'Hamilton': [14570, 14824, 15012, 15140, 15231, 15300],
        'Hardee': [27443, 27464, 27483, 27500, 27515, 27529],
        'Hendry': [40953, 42898, 44380, 45554, 46570, 47468],
        'Hernando': [192186, 206365, 218237, 227500, 235005, 241532],
        'Highlands': [104834, 108990, 112385, 115203, 117667, 119883],
        'Hillsborough': [1478759, 1614227, 1723500, 1811841, 1889150, 1958324],
        'Holmes': [20001, 20067, 20128, 20181, 20230, 20275],
        'Indian River': [158834, 171332, 181673, 189917, 196897, 203110],
        'Jackson': [46587, 47096, 47507, 47721, 47827, 47870],
        'Jefferson': [14394, 14558, 14708, 14843, 14965, 15079],
        'Lafayette': [8690, 9044, 9340, 9568, 9756, 9920],
        'Lake': [366742, 409201, 445438, 475796, 501692, 525207],
        'Lee': [750493, 829303, 894597, 948834, 996086, 1038511],
        'Leon': [299484, 312338, 323012, 331425, 338510, 344579],
        'Levy': [41699, 43115, 44260, 45176, 45947, 46650],
        'Liberty': [8575, 8848, 9068, 9229, 9354, 9459],
        'Madison': [18954, 19038, 19114, 19181, 19242, 19298],
        'Manatee': [398503, 437640, 470632, 498045, 522641, 544365],
        'Marion': [368135, 394914, 417138, 434244, 448104, 459981],
        'Martin': [161301, 170496, 177612, 183467, 188675, 193311],
        'Miami-Dade': [2832794, 2992713, 3128267, 3234615, 3322226, 3398177],
        'Monroe': [77823, 78799, 79424, 79793, 80020, 80159],
        'Nassau': [89258, 99151, 107454, 114621, 121087, 126888],
        'Okaloosa': [203951, 214634, 223161, 230024, 236005, 241122],
        'Okeechobee': [42112, 43443, 44497, 45314, 46043, 46698],
        'Orange': [1415260, 1558673, 1678397, 1777854, 1864282, 1941833],
        'Osceola': [387055, 453633, 512481, 560690, 603577, 643089],
        'Palm Beach': [1466494, 1544853, 1612167, 1668575, 1716971, 1758539],
        'Pasco': [542638, 592955, 635684, 668774, 696407, 720542],
        'Pinellas': [984054, 1011799, 1031377, 1045155, 1055506, 1063764],
        'Polk': [715090, 783145, 840192, 888368, 929316, 965766],
        'Putnam': [73723, 74225, 74692, 75096, 75451, 75772],
        'Saint Johns': [261900, 304567, 340548, 370871, 398005, 422755],
        'Saint Lucie': [322265, 355760, 384794, 407451, 426418, 443052],
        'Santa Rosa': [184653, 201790, 215932, 227843, 238660, 248474],
        'Sarasota': [438816, 472115, 498160, 520376, 539897, 557545],
        'Seminole': [476727, 505142, 528478, 548354, 565100, 579426],
        'Sumter': [141422, 167786, 189956, 208161, 223844, 237883],
        'Suwannee': [45463, 47232, 48716, 49888, 50841, 51669],
        'Taylor': [22436, 22762, 22994, 23148, 23247, 23315],
        'Union': [15410, 15603, 15722, 15784, 15817, 15833],
        'Volusia': [551588, 583919, 608945, 628786, 646107, 662049],
        'Wakulla': [33981, 36383, 38402, 40070, 41429, 42582],
        'Walton': [74724, 85868, 95460, 103610, 110913, 117864],
        'Washington': [25334, 26178, 26835, 27326, 27720, 28052],
        'FLORIDA': [21596068, 23138553, 24419127, 25461863, 26356415, 27149835],
}

    # Add all other counties here...

# Creating a dictionary to store the growth rates
growth_rates = {}

# Calculate the growth rate for each county across the 5-year periods
for county, populations in population_data.items():
    growth_rates[county] = []
    for i in range(1, len(populations)):
        rate = calculate_cagr(populations[i - 1], populations[i], 5)
        growth_rates[county].append(rate)

# Converting to a DataFrame for better visualization
growth_rate_df = pd.DataFrame(growth_rates, index=["2020-2025", "2025-2030", "2030-2035", "2035-2040", "2040-2045"]).transpose()

print(growth_rate_df)

# Save the DataFrame (growth_rate_df) as an Excel file in the current directory
file_path = 'growth_rates.xlsx'
growth_rate_df.to_excel(file_path, index=False)

print(f"Excel file generated as {file_path}")