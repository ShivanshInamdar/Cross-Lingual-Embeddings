The score.py file takes in a file that has format:

word gold pred pred pred pred pred

The score.py file can be run on the command file as follows:

python score.py filename 5 0

to reproduce our results. The 5 corresponds to the number of preds. The 0 is for the edit distance leeway we allow for.

Example of the input is:

torpedo torpille torpille torpilles anti-torpille grenadeur anti-sous-marines
chat bavardage tchat tchatter tchate tchats chatroom
chat chat tchat tchatter tchate tchats chatroom

We apologise about the naming of the files.

here's a short translation:

baseline_en_fr.txt --- published baseline en->fr
opposite_baseline.txt --- published baseline fr->en
ext1_en_fr.txt --- extension 1 en->fr
ext1testoutput_opposite.txt --- extension 1 fr->en
no_dict_ext2_en_fr.txt --- extension 2 en->fr
opposite_ext2.txt --- extension 2 fr->en
ext3_en_fr.txt --- extension 3 en->fr
ext3testoutput_opposite.txt --- extension 3 fr->en