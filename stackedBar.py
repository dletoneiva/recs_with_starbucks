import BeautifulChart as bc
import matplotlib.pyplot as plt

class stackedBar(bc.Chart):
    """
    Plots a stacked bar pattern for the data. Better used for part-all
    comparisons (like how a team behaves compared to the overall company).

    Attributes:
        localValues (float): array of values to be plotted (local)
        overallValues (float): array of values to be plotted in the overall view
        categories (string): array of strings containing categories

    Future improvements:
        - Order the categories by bar sizes
    """
    def __init__(self, 
                 localValues,
                 overallValues,
                 categories):

        self.localValues = localValues
        self.overallValues = overallValues
        self.categories = categories
        
        bc.Chart.__init__(self)
    
    def plot(self):
        """
        Plots given data.

        Args: 
            None
        
        Returns:
            None
        """
        # creates a new figure
        fig, ax = plt.subplots(1,1,figsize=(10,10))

        # plots the data
        ax.barh(self.categories,
                self.overallValues,
                color=self.primaryColorPalette[1])

        ax.barh(self.categories,
                self.localValues,
                color=self.primaryColorPalette[0])

        ax.invert_yaxis()

        # add labels with counts
        for i, v in enumerate(self.localValues):
            ax.annotate(v,xy=(v-1,i),va='center',fontsize=12,color='white')

        for i, v in enumerate(self.overallValues):
            ax.annotate(v,xy=(v-0.7,i),va='center',fontsize=12,color='white')

        # remove axes
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.tick_params(
            axis='both',       # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            left=False,        # ticks along the left edge are off
            labelbottom=False) # labels along the bottom edge are off

        # adjusts aesthetics
        plt.rc('ytick', labelsize=12)
        plt.rc('legend', fontsize=12)

        # sets further information
        if not self.title:
            ax.set_title(self.title,fontsize=16)

        if self.useLegend == 1:
            plt.legend(self.legend,loc='best')

        if self.saveFigures == 1:
            if self.title != '':
                plt.savefig(self.title + '.png')
            else:
                plt.savefig('output.png')




