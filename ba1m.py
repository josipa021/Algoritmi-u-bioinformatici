{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "ba1m.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyM195zgQh+cmXlJr32jmNE/"
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
      "cell_type": "markdown",
      "source": [
        "**Implement NumberToPattern**\n",
        "\n",
        "Convert an integer to its corresponding DNA string.\n",
        "\n",
        "Given: Integers index and k.\n",
        "\n",
        "Return: NumberToPattern(index, k)."
      ],
      "metadata": {
        "id": "h5wCxGFdN3ka"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "uqSnZ-VYNzED"
      },
      "outputs": [],
      "source": [
        "def NumberToSymbol(num):\n",
        "\n",
        "    if num == 0:\n",
        "        return \"A\"\n",
        "    if num == 1:\n",
        "        return \"C\"\n",
        "    if num == 2:\n",
        "        return \"G\"\n",
        "    if num == 3:\n",
        "        return \"T\""
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def NumberToPattern(index,k):\n",
        "\n",
        "    if k == 1:\n",
        "        return NumberToSymbol(index)\n",
        "\n",
        "    remainder = index % 4\n",
        "    index = index // 4\n",
        "    pattern = NumberToPattern(index,k-1) \n",
        "    return pattern + NumberToSymbol(remainder)"
      ],
      "metadata": {
        "id": "cDXh-47AOJKl"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(NumberToPattern(8180,8))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v0z-18c9OTgi",
        "outputId": "39a83c97-cbba-4c07-cd04-eb9293e33278"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ACTTTTCA\n"
          ]
        }
      ]
    }
  ]
}