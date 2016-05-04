# got-predictions

Making predictions about season 6 of Game of Thrones. Scrapes the text from the TV show wiki.

Run as follows:

* got-wiki-data.ipynb - extracts data from the wiki
    * note, this data has been saved as a zip from an extract before season 6
    * probably the wiki will be "contaminated" as episodes of season 6 come out
* got-parse-data.ipynb - this removes characters from the wiki who are not in the TV show
* got-mortality-prediction.ipynb - runs a few models - the most noteable is TF-IDF on all the text up to but *excluding* the season a character died

Cross-fold AUROC of the last model is around ~0.8, which is better than I expected, but could be due to information leakage.

The model is trained to classify those from seasons 1-5 as alive/dead.
I'm treating false positives of the model as the "predictions" for season 6.

Top 10 predictions:

```
Robin_Arryn          - 94.07%
Tommen_Baratheon     - 74.46%
Rickon_Stark         - 72.01%
Tyrion_Lannister     - 67.81%
Daenerys_Targaryen   - 66.70%
Tysha                - 65.88%
Arya_Stark           - 63.93%
Bran_Stark           - 62.56%
Davos_Seaworth       - 54.56%
Sansa_Stark          - 53.89%
```

Note: somebody informed me Tysha already died... oops...
