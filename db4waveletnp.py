import numpy as np

class Daubechies4WaveletTransform:
    """
    Class to perform the Discrete Wavelet Transform (DWT) and Inverse DWT (IDWT)
    using the Daubechies 4 wavelet.
    """

    def __init__(self):
        # Daubechies 4 wavelet filter coefficients
        self.decomp_low = np.array([-0.010597401784997278, 0.032883011666982945, 0.030841381835986965,
                                   -0.18703481171888114, -0.02798376941698385, 0.6308807679295904,
                                   0.7148465705525415, 0.23037781330885523])
        self.decomp_high = np.array([-0.23037781330885523, 0.7148465705525415, -0.6308807679295904,
                                    -0.02798376941698385, 0.18703481171888114, 0.030841381835986965,
                                    -0.032883011666982945, -0.010597401784997278])
        self.recon_low = np.array([0.23037781330885523, 0.7148465705525415, 0.6308807679295904,
                                  -0.02798376941698385, -0.18703481171888114, 0.030841381835986965,
                                  0.032883011666982945, -0.010597401784997278])
        self.recon_high = np.array([-0.010597401784997278, -0.032883011666982945, 0.030841381835986965,
                                   0.18703481171888114, -0.02798376941698385, -0.6308807679295904,
                                   0.7148465705525415, -0.23037781330885523])

    def dwt(self, arr_time, level):
        """
        Discrete Wavelet Transform

        Parameters
        ----------
        arr_time: numpy.ndarray
            Input array in the Time domain.
        level: int
            Level to decompose.

        Returns
        -------
        numpy.ndarray
            Output array in the Frequency or Hilbert domain.
        """
        n = len(arr_time)
        a = level // 2

        # Compute approximation and detail coefficients
        approx = np.convolve(arr_time, self.decomp_low, 'valid')
        detail = np.convolve(arr_time, self.decomp_high, 'valid')

        # Downsample the coefficients
        arr_hilbert = np.concatenate((approx[::2], detail[::2]))

        return arr_hilbert

    def idwt(self, arr_hilbert, level):
        """
        Inverse Discrete Wavelet Transform

        Parameters
        ----------
        arr_hilbert: numpy.ndarray
            Input array in the Frequency or Hilbert domain.
        level: int
            Level to decompose.

        Returns
        -------
        numpy.ndarray
            Output array in the Time domain.
        """
        n = len(arr_hilbert)
        a = level // 2

        # Upsample the coefficients
        approx = np.repeat(arr_hilbert[:a], 2)
        detail = np.repeat(arr_hilbert[a:], 2)

        # Reconstruct the time-domain signal
        arr_time = np.convolve(approx, self.recon_low, 'full') + \
                   np.convolve(detail, self.recon_high, 'full')

        return arr_time[:level]