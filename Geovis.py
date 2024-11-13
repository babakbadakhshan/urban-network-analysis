{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMHvBEnT/Ue7koGAq8KmVlW"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "import geopandas as gpd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import contextily as ctx\n",
        "\n",
        "\n",
        "gdf = gpd.read_file('250GRIDDED.gpkg')\n",
        "\n",
        "print(gdf.head())\n",
        "print(gdf.columns)\n",
        "\n",
        "def categorize(Seconds):\n",
        "    if Seconds >= 1500:\n",
        "      return 30\n",
        "    elif 1200 < Seconds < 1500:\n",
        "      return 25\n",
        "    elif 900 < Seconds < 1200:\n",
        "      return 20\n",
        "    elif 600 < Seconds < 900:\n",
        "      return 15\n",
        "    elif 300 < Seconds < 600:\n",
        "      return 10\n",
        "    elif 0 < Seconds < 300:\n",
        "      return 5\n",
        "    else:\n",
        "      return np.nan\n",
        "\n",
        "gdf['Minutes'] = gdf['Seconds'].apply(categorize)\n",
        "print(gdf[['Seconds', 'Minutes']].head())\n",
        "\n",
        "f, ax = plt.subplots(1,1,figsize=(20,20))\n",
        "\n",
        "gdf.plot(column=\"Minutes\", ax=ax, cmap = 'magma', edgecolor='black')\n",
        "cbar = plt.colorbar(ax.collections[0], ax=ax, orientation='vertical', fraction=0.025, pad=0)\n",
        "#ctx.add_basemap(ax, source=ctx.providers.Stamen.TonerLite)\n",
        "cbar.set_label('Walking Time / Minutes', fontsize=20)\n",
        "cbar.ax.tick_params(labelsize=15)\n",
        "ax.set_title('Access to different types of facilities within a 15-minute walk', fontsize=25)\n",
        "ax.axis('off')\n",
        "plt.show()\n",
        "\n",
        "#gdf.to_file(\"250GRIDDED_v2.gpkg\")"
      ],
      "metadata": {
        "id": "8yXaLHNJZWvo"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}