import seaborn as sns

class Chart: 
    """
    Mother class that allows the plots.

    Future improvements:
        - Test for hex strings in color palettes.
    """

    def __init__(self):
        """
        Initializes the chart object with default values.

        Attributes:

            primaryColorPalette (list of 5 hex): list containing the primary 
            color palette (RGB)

            secondaryColorPalette (list of 4 hex): list containing the secondary 
            color palette (RGB)

            saveFigures (bool): default is to save figures at the same folder

            title (string): title to be put at the figure

            useLegend (bool): default is not to use legends

            legend (list of strings): legends to be put at
        """
        self.primaryColorPalette = ['#DB6B2E',
                                    '#E28958',
                                    '#E9A682',
                                    '#F1C4AB',
                                    '#F8E1D5'] # set in orange colors
        
        self.secondaryColorPalette = ['#CF3779',
                                      '#ADC242',
                                      '#432466',
                                      '#55A8B5'] # set in happy colors
        self.saveFigures=1,
        self.useLegend = 0,
        self.title = "",
        self.legend = []


    def changeColorPalettePrimary(self, colorPalette, showPalette=1):
        """
        Changes the primary color palette, low conspicuity uses

        Args:
            color_palette: list of 5 hex codes for RGB
        
        Returns:
            None

        """
        if len(colorPalette)!= 5:
            return 'Incompatible list size.'
        else:
            self.primaryColorPalette = colorPalette
            if showPalette == 1: # shows the palette for the user
                sns.palplot(colorPalette)

            return self.primaryColorPalette

    def changeColorPaletteSecondary(self, colorPalette, showPalette=1):
        """
        Changes the secondary color palette, high conspicuity uses

        Args:
            color_palette: list of 4 hex codes for RGB
        
        Returns:
            None

        """
        if len(colorPalette)!= 4:
            return 'Incompatible list size.'
        else:
            self.primaryColorPalette = colorPalette
            if showPalette == 1: # shows the palette for the user
                sns.palplot(colorPalette)

            return self.primaryColorPalette
    
    def changeProperties(self,
                         saveFigures=1,
                         useLegend = 0,
                         title = '',
                         legend = []):
        """
            Changes the default properties.

            Args: 
                see parent class.

            Returns:
                None
        """

        self.saveFigures = saveFigures
        self.title = title
        self.useLegend =useLegend
        self.legend = legend