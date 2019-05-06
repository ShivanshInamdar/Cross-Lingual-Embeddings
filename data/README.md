We have used a few different types of data:
    1. Pre-trained word vectors for 157 languages from fastText. We have included samples for the french and english word vector files. We will expand to more languages later in the project. The files here are in .vec form and are converted to .magnitude to allow us to work with them using pymagnitude.
    Link to fastText word vector page: https://fasttext.cc/docs/en/crawl-vectors.html
    2. A dictionary of data separated into 2 parts for train and test. We obtained the dictionary form facebook reasearch's MUSE project.
    Link to bilingual dictionaires page: https://github.com/facebookresearch/MUSE#ground-truth-bilingual-dictionaries


The first dataset has lines of a word and coordinates specifying the vector associated to the word.

The second one has english-french word pairs that are blankspace separated. These are simple text files. Some examples are:

pursuit poursuite
reserved réservés
johns johns
verified vérifié
proportion proportions
porter portier
twins jumelles