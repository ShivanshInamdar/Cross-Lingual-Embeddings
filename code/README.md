Running baseline code is:

python baseline_newer.py en_vecs fr_vecs en_fr_dict test_file filename_to_write direction

We use english.magnitude as en_vecs
french.magnitude as fr_vecs
en-fr.0-5000.txt as en_fr_dict
test.txt as test_file
Direction can be either en-fr or fr-en

Running extension 1 is:

python extension_1.py english.magnitude french.magnitude en-fr.0-5000.txt test.txt filename_to_write alpha direction

we use alpha 0.1

where direction can be either en-fr or fr-en

Running extension 2 is:

python extension_2.py english.magnitude french.magnitude test.txt filename_to_write direction

Running extension 3 is:

python extension_3.py english.magnitude french.magnitude en-fr.0-5000.txt test.txt filename_to_write direction