# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# test function by updating damages
# -------------------------------
# 1. Update Recorded Damages
# -------------------------------
def update_damages(damages_list):
    conversion = {"M": 1_000_000, "B": 1_000_000_000}
    updated = []
    for damage in damages_list:
        if damage == "Damages not recorded":
            updated.append(damage)
        else:
            if damage[-1] in conversion:
                updated.append(float(damage[:-1]) * conversion[damage[-1]])
            else:
                updated.append(float(damage))
    return updated

updated_damages = update_damages(damages)
#print(updated_damages)

# -------------------------------
# 2. Create Hurricanes Dictionary
# -------------------------------
def create_hurricane_dict(names, months, years, winds, areas, damages, deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": winds[i],
            "Areas Affected": areas[i],
            "Damage": damages[i],
            "Deaths": deaths[i]
        }
    return hurricanes

hurricanes = create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricanes["Cuba I"])

# -------------------------------
# 3. Organize by Year
# -------------------------------
def hurricanes_by_year(hurricane_dict):
    hurricanes_year = {}
    for hurricane in hurricane_dict.values():
        year = hurricane["Year"]
        hurricanes_year.setdefault(year, []).append(hurricane)
    return hurricanes_year

hurricanes_year = hurricanes_by_year(hurricanes)
#print(hurricanes_year[1932])

# -------------------------------
# 4. Count Affected Areas
# -------------------------------
def count_affected_areas(hurricane_dict):
    area_count = {}
    for hurricane in hurricane_dict.values():
        for area in hurricane["Areas Affected"]:
            area_count[area] = area_count.get(area, 0) + 1
    return area_count

affected_area_count = count_affected_areas(hurricanes)
#print(affected_area_count)

# -------------------------------
# 5. Area Most Frequently Hit
# -------------------------------
def most_affected_area(area_count):
    max_area = max(area_count, key=area_count.get)
    return max_area, area_count[max_area]

max_area, max_hits = most_affected_area(affected_area_count)
#print(max_area, max_hits)

# -------------------------------
# 6. Deadliest Hurricane
# -------------------------------
def deadliest_hurricane(hurricane_dict):
    deadliest = max(hurricane_dict.values(), key=lambda x: x["Deaths"])
    return deadliest["Name"], deadliest["Deaths"]

deadliest_name, deadliest_deaths = deadliest_hurricane(hurricanes)
#print(deadliest_name, deadliest_deaths)

# -------------------------------
# 7. Mortality Rating
# -------------------------------
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}

def rate_hurricanes_by_mortality(hurricane_dict, scale):
    rating_dict = {k: [] for k in scale.keys()}
    for hurricane in hurricane_dict.values():
        deaths = hurricane["Deaths"]
        rating = 0
        for k, upper in scale.items():
            if deaths <= upper:
                rating = k
                break
        rating_dict[rating].append(hurricane)
    return rating_dict

mortality_ratings = rate_hurricanes_by_mortality(hurricanes, mortality_scale)
#print(mortality_ratings[4])

# -------------------------------
# 8. Hurricane Causing Most Damage
# -------------------------------
def most_damaging_hurricane(hurricane_dict):
    max_damage = 0
    hurricane_name = ""
    for hurricane in hurricane_dict.values():
        damage = hurricane["Damage"]
        if damage != "Damages not recorded" and damage > max_damage:
            max_damage = damage
            hurricane_name = hurricane["Name"]
    return hurricane_name, max_damage

most_damaging_name, most_damaging_value = most_damaging_hurricane(hurricanes)
#print(most_damaging_name, most_damaging_value)

# -------------------------------
# 9. Rating Hurricanes by Damage
# -------------------------------
damage_scale = {0: 0, 1: 100_000_000, 2: 1_000_000_000, 3: 10_000_000_000, 4: 50_000_000_000}

def rate_hurricanes_by_damage(hurricane_dict, scale):
    rating_dict = {k: [] for k in scale.keys()}
    for hurricane in hurricane_dict.values():
        damage = hurricane["Damage"]
        if damage == "Damages not recorded":
            continue
        rating = 0
        for k, upper in scale.items():
            if damage <= upper:
                rating = k
                break
        rating_dict[rating].append(hurricane)
    return rating_dict

damage_ratings = rate_hurricanes_by_damage(hurricanes, damage_scale)
#print(damage_ratings[4])
