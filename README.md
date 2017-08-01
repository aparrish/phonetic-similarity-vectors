# Poetic sound similarity vectors using phonetic features

This is the source code used to implement the algorithms, experiments and
applications in my forthcoming paper, "Poetic sound similarity vectors using
phonetic features." The source code is written in Python.

## Dependencies

Almost everything should be covered in a standard Anaconda install, i.e.:

* pandas
* matplotlib
* numpy
* scikit-learn

You'll also need [spaCy](http://spacy.io) and
[Annoy](https://pypi.python.org/pypi/annoy) for some of the applications, which
you can install with `pip` or through `conda-forge`. For spaCy:

    conda config --add channels conda-forge
    conda install spacy
    python -m spacy download en_core_web_md

For Annoy:

    conda config --add channels conda-forge
    conda install python-annoy

(Note: You don't need any of this stuff if you just want to play around with
the pre-computed vectors! Though I definitely recommend using a fast
nearest-neighbor search library like Annoy.)

## Files

### CMU Dict and pre-computed vectors

The file `cmudict-0.7b-with-vitz-nonce` contains the most current (as of this
writing) version of the [CMU Pronouncing
Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict), edited to include
the "nonce" words from [Vitz and Winkler
(1973)](https://www.researchgate.net/publication/232418589_Predicting_the_Judged_Similarity_of_Sound_of_English_words).

The file `cmudict-0.7b-simvecs` contains pre-computed vectors for all of the
words in `cmudict-0.7b-with-vitz-nonce`. This is probably the file you want if
you just want to play around with the vectors! The vectors are formatted just
like the CMU Pronouncing Dictionary (i.e., word in all caps, two spaces, then
space-separated values per dimension).

### Python source

Run `generate.py` to create your own set of vectors from a CMU Pronouncing
Dictionary source file. Pass the dictionary as input and redirect the output to
your desired file, e.g.:

    PYTHONIOENCODING=latin1 python generate.py <cmudict-0.7b-with-vitz-nonce >cmudict-0.7b-simvecs

Note that you *must* specify `latin1` encoding when running this script (unless
your dictionary uses some other character set).

The `similarity.py` script is a quick script for checking your vectors. Pass
the file with your similarity vectors as a command line argument, and the
program will respond to every line of standard input with the most similar
items from the embedding:

    $ python similarity.py cmudict-0.7b-simvecs
    loading...
    done.
    ELEPHANT
    ['ELEPHANT', "ELEPHANT'S", 'ELEPHANTS', "ELEPHANTS'", 'ENTOFFEN', 'UFFELMAN', 'UNRUFFLED', 'MUFFLE', "ENTOFFEN'S", 'KALAFUT']
    AARDVARK
    ['AARDVARK', 'AARDVARKS', 'AARGH', 'ARGH', 'ARC', 'ARK', 'ARB', 'ARTCARVED', 'ALSGAARD', 'ARCHARD']
    BADGER
    ['BADGER', 'BADER', 'BATHER(1)', 'BADGERED', 'BISER', "BADGER'S", 'BADGERS', 'BADDERS', 'MADAR', 'MADDER']
    DOLPHIN
    ['DOLPHIN', 'DOLPHINS', "DOLPHINS'", 'DALFEN', 'GALVEN', 'DONELSON', 'GALVAN', 'JARVIS', 'GALVESTON', 'DARTH']

Hit `^D` when you're done.

Finally, `featurephone.py` contains a few helper functions that help build the
bigram analysis of the dictionary.

### Jupyter notebooks

* `experiment.ipynb` contains the code to run the experiments comparing the
  phonetic similarity reported by the embeddings in my paper to the similarity
  scores obtained from human subjects in Vitz and Winkler (1973).
* `some-applications.ipynb` contains a number of playful and poetic
  experimental applications of the phonetic similarity embeddings (including
  sound analogies, averages, symbolism tinting, etc.)

Still forthcoming: An example of how to use the embeddings for longer stretches
of text, as in the "random walk" example in the paper.

## License

See `LICENSE`, which applies to everything in this repository except the copy
of the CMU Pronouncing Dictionary, which is used under the terms of their
license (included in the header of the file).
