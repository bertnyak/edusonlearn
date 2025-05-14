def sum_n_dimensional_vectors(vectors):
    result = [0] * len(vectors[0])
    for vector in vectors:
        result = map(sum, zip(result, vector))

    return tuple(result)
sum_n_dimensional_vectors(vectors='sas')