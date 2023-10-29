import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The result of multiplying m_a and m_b.

    Raises:
        ValueError: If m_a or m_b are not valid for matrix multiplication.
    """
    try:
        result = np.dot(np.array(m_a), np.array(m_b))
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
