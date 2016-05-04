# got-analysis

Making predictions about season 6 of Game of Thrones. Scrapes the text from the TV show wiki.

Run as follows:

* got-wiki-data.ipynb - extracts data from the wiki
    * note, this data has been saved as a zip from an extract before season 6
    * probably the wiki will be "contaminated" as episodes of season 6 come out
* got-parse-data.ipynb - this removes characters from the wiki who are not in the TV show
* got-mortality-prediction.ipynb - runs a few models - the most noteable is TF-IDF on all the text up to but *excluding* the season a character died

Cross-fold AUROC of the last model is around ~0.8, which is better than I expected, but could be due to information leakage.
