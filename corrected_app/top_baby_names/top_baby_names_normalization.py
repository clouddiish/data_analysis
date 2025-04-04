states = {
    "AK": 2,
    "AL": 4,
    "AR": 6,
    "AZ": 8,
    "CA": 10,
    "CO": 12,
    "CT": 14,
    "DC": 16,
    "DE": 18,
    "FL": 20,
    "GA": 22,
    "HI": 24,
    "IA": 26,
    "ID": 28,
    "IL": 30,
    "IN": 32,
    "KS": 34,
    "KY": 36,
    "LA": 38,
    "MA": 40,
    "MD": 42,
    "ME": 44,
    "MI": 46,
    "MN": 48,
    "MO": 50,
    "MS": 52,
    "MT": 54,
    "NC": 56,
    "ND": 58,
    "NE": 60,
    "NH": 62,
    "NJ": 64,
    "NM": 66,
    "NV": 68,
    "NY": 70,
    "OH": 72,
    "OK": 74,
    "OR": 76,
    "PA": 78,
    "RI": 80,
    "SC": 82,
    "SD": 84,
    "TN": 86,
    "TX": 88,
    "UT": 90,
    "VA": 92,
    "VT": 94,
    "WA": 96,
    "WI": 98,
    "WV": 100,
    "WY": 102,
}
sex = {"F": 50, "M": 100}
names = {
    "Mary": 1,
    "Linda": 2,
    "Debra": 3,
    "Lisa": 4,
    "Michelle": 5,
    "Jennifer": 6,
    "Jessica": 7,
    "Samantha": 8,
    "Ashley": 9,
    "Hannah": 10,
    "Madison": 11,
    "Emma": 12,
    "Isabella": 13,
    "Olivia": 14,
    "Kimberly": 15,
    "Angela": 16,
    "Amanda": 17,
    "Emily": 18,
    "Mia": 19,
    "Sophia": 20,
    "Barbara": 21,
    "Susan": 22,
    "Karen": 23,
    "Patricia": 24,
    "Alexis": 25,
    "Kayla": 26,
    "Katherine": 27,
    "Deborah": 28,
    "Donna": 29,
    "Sarah": 30,
    "Ava": 31,
    "Brittany": 32,
    "Helen": 33,
    "Shirley": 34,
    "Carol": 35,
    "Taylor": 36,
    "Chloe": 37,
    "Betty": 38,
    "Sharon": 39,
    "Julie": 40,
    "Lori": 41,
    "Addison": 42,
    "Dorothy": 43,
    "Samantha": 44,
    "Margaret": 45,
    "Megan": 46,
    "Jasmine": 47,
    "Melissa": 48,
    "Judith": 49,
    "Nancy": 50,
    "Sandra": 51,
    "Joan": 52,
    "Alyssa": 53,
    "Ruth": 54,
    "Cindy": 55,
    "Brenda": 56,
    "John": 57,
    "Robert": 58,
    "Michael": 59,
    "David": 60,
    "Christopher": 61,
    "Jacob": 62,
    "Ethan": 63,
    "James": 64,
    "Aiden": 65,
    "William": 66,
    "Mason": 67,
    "Justin": 68,
    "Jason": 69,
    "Joshua": 70,
    "Angel": 71,
    "Anthony": 72,
    "Daniel": 73,
    "Alexander": 74,
    "Liam": 75,
    "Matthew": 76,
    "Ryan": 77,
    "Jayden": 78,
    "George": 79,
    "Richard": 80,
    "Noah": 81,
    "Carter": 82,
    "Tyler": 83,
    "Logan": 84,
    "Samuel": 85,
    "Elijah": 86,
    "Larry": 87,
    "Austin": 88,
    "Owen": 89,
    "Wyatt": 90,
    "Jose": 91,
    "Joe": 92,
    "Isaiah": 93,
    "Benjamin": 94,
    "Nicholas": 95,
    "Andrew": 96,
}


def top_baby_names_normalize_row(raw_row: list) -> list:
    """Normalizes a row of raw baby name data.

    This function converts state, sex, year, name, and occurrence values into a standardized format
    using predefined mappings and transformations.

    Args:
        raw_row (list): A list containing raw data for a baby name entry.

    Returns:
        list: A normalized list where:
            - Index 0: Mapped state value.
            - Index 1: Mapped sex value.
            - Index 2: Year normalized by subtracting 1910.
            - Index 3: Mapped name value.
            - Index 4: Scaled occurrence value (multiplied by 0.02).
    """
    normalized_row = []
    normalized_row.append(states[raw_row[0]])
    normalized_row.append(sex[raw_row[1]])
    normalized_row.append(int(raw_row[2]) - 1910)
    normalized_row.append(names[raw_row[3]])
    normalized_row.append(0.02 * int(raw_row[4]))
    return normalized_row


def top_baby_names_denormalize_row(normalized_row: list) -> list:
    """Reverses the normalization process to retrieve approximate original values.

    Args:
        normalized_row (list): A list containing normalized baby name data.

    Returns:
        list: An approximate original row where:
            - Index 0: Closest matching state abbreviation.
            - Index 1: Closest matching sex value.
            - Index 2: Year restored by adding 1910.
            - Index 3: Closest matching name.
            - Index 4: Occurrence count approximated.
    """

    def find_closest_value(dictionary, target_value):
        return min(dictionary, key=lambda k: abs(dictionary[k] - target_value))

    original_row = []
    original_row.append(find_closest_value(states, normalized_row[0]))
    original_row.append(find_closest_value(sex, normalized_row[1]))
    original_row.append(int(normalized_row[2]) + 1910)
    original_row.append(find_closest_value(names, normalized_row[3]))
    original_row.append(int(normalized_row[4] / 0.02))

    return original_row
