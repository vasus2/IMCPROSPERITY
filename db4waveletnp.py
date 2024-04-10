class DB4WaveletTransform:
    """
    Class to run the selected wavelet and to perform the dwt & idwt
    based on the wavelet filters

    Attributes
    ----------
    __wavelet__: object
        object of the selected wavelet class
    """



    def __init__(self):
        self.__name__ = "Daubechies Wavelet 4"
        self.__motherWaveletLength__ = 8  # length of the mother wavelet
        self.__transformWaveletLength__ = 2  # minimum wavelength of input signal

        # decomposition filter
        # low-pass
        self.decompositionLowFilter = [
            -0.010597401784997278,
            0.032883011666982945,
            0.030841381835986965,
            - 0.18703481171888114,
            - 0.02798376941698385,
            0.6308807679295904,
            0.7148465705525415,
            0.23037781330885523
        ]

        # high-pass
        self.decompositionHighFilter = [
            -0.23037781330885523,
            0.7148465705525415,
            - 0.6308807679295904,
            - 0.02798376941698385,
            0.18703481171888114,
            0.030841381835986965,
            - 0.032883011666982945,
            - 0.010597401784997278,
        ]

        # reconstruction filters
        # low pass
        self.reconstructionLowFilter = [
            0.23037781330885523,
            0.7148465705525415,
            0.6308807679295904,
            - 0.02798376941698385,
            - 0.18703481171888114,
            0.030841381835986965,
            0.032883011666982945,
            - 0.010597401784997278,
        ]

        # high-pass
        self.reconstructionHighFilter = [
            -0.010597401784997278,
            - 0.032883011666982945,
            0.030841381835986965,
            0.18703481171888114,
            - 0.02798376941698385,
            - 0.6308807679295904,
            0.7148465705525415,
            - 0.23037781330885523,
        ]

    def dwt(self, arrTime, level):
        """
        Discrete Wavelet Transform

        Parameters
        ----------
        arrTime : array_like
            input array in Time domain
        level : int
            level to decompose

        Returns
        -------
        array_like
            output array in Frequency or the Hilbert domain
        """
        arrHilbert = [0.] * level
        # shrinking value 8 -> 4 -> 2
        a = level >> 1

        for i in range(a):
            for j in range(self.__motherWaveletLength__):
                k = (i << 1) + j

                # circulate the array if scale is higher
                while k >= level:
                    k -= level

                # approx & detail coefficient
                arrHilbert[i] += arrTime[k] * self.decompositionLowFilter[j]
                arrHilbert[i + a] += arrTime[k] * self.decompositionHighFilter[j]

        return arrHilbert

    def idwt(self, arrHilbert, level):
        """
        Inverse Discrete Wavelet Transform

        Parameters
        ----------
        arrHilbert : array_like
            input array in Frequency or the Hilbert domain
        level : int
            level to decompose

        Returns
        -------
        array_like
            output array in Time domain
        """
        arrTime = [0.] * level
        # shrinking value 8 -> 4 -> 2
        a = level >> 1

        for i in range(a):
            for j in range(self.__motherWaveletLength__):
                k = (i << 1) + j

                # circulating the array if scale is higher
                while k >= level:
                    k -= level

                # summing the approx & detail coefficient
                arrTime[k] += (arrHilbert[i] * self.reconstructionLowFilter[j] +
                               arrHilbert[i + a] * self.reconstructionHighFilter[j])

        return arrTime