from typing import Callable


def get_random_centroids(how_many: int, randomizer_function: Callable[[], list]) -> list:
    """Generates a specified number of random centroids using a given randomizer function.

    Args:
        how_many (int): The number of centroids to generate.
        randomizer_function (Callable[[], list]): A function that generates a random centroid.

    Returns:
        list: A list of randomly generated centroids.
    """
    return [randomizer_function() for _ in range(how_many)]


def get_closest_centroid_id(
    centroids: list,
    datapoint: list,
    exclude_attributes_ids: list,
    calculate_distance_function: Callable[[list, list, list], list],
) -> int:
    """Finds the index of the centroid closest to a given data point.

    Args:
        centroids (list): A list of centroid points.
        datapoint (list): A single data point.
        exclude_attributes_ids (list): Indices of attributes to be excluded from distance calculations.
        calculate_distance_function (Callable[[list, list, list], list]): A function that calculates
            distance between two points, excluding specified attributes.

    Returns:
        int: The index of the closest centroid.
    """
    min_distance = float("inf")
    min_index = -1
    for i, centroid in enumerate(centroids):
        distance = calculate_distance_function(centroid, datapoint, exclude_attributes_ids)
        if distance < min_distance:
            min_distance = distance
            min_index = i
    return min_index


def get_clusters(
    centroids: list,
    datapoints: list,
    exclude_attributes_ids: list,
    calculate_distance_function: Callable[[list, list, list], list],
) -> list:
    """Groups data points into clusters based on their closest centroid.

    Args:
        centroids (list): A list of centroids.
        datapoints (list): A list of data points to be clustered.
        exclude_attributes_ids (list): Indices of attributes to be excluded from distance calculations.
        calculate_distance_function (Callable[[list, list, list], list]): A function that calculates
            distance between two points, excluding specified attributes.

    Returns:
        list: A list of clusters, where each cluster is a list of data points assigned to a centroid.
    """
    clusters = [[] for _ in centroids]

    for datapoint in datapoints:
        closest_centroid_id = get_closest_centroid_id(
            centroids, datapoint, exclude_attributes_ids, calculate_distance_function
        )
        clusters[closest_centroid_id].append(datapoint)

    return clusters


def get_new_centroids(
    clusters: list, find_centroid_function: Callable[[list], list], randomizer_function: Callable[[], list]
) -> list:
    """Computes new centroids for each cluster, handling empty clusters by generating random centroids.

    Args:
        clusters (list): A list of clusters, where each cluster is a list of data points.
        find_centroid_function (Callable[[list], list]): A function that computes the centroid of a given cluster.
        randomizer_function (Callable[[], list]): A function that generates a random centroid for empty clusters.

    Returns:
        list: A list of updated centroids.
    """
    new_centroids = []
    for cluster in clusters:
        if len(cluster) == 0:
            new_centroids.append(randomizer_function())
        else:
            new_centroids.append(find_centroid_function(cluster))
    return new_centroids
