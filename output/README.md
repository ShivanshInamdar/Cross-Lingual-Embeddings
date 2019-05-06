The score.py file takes in a file that has format:

word gold pred pred pred pred pred

The score.py file can be run on the command file as follows:

python score.py filename 5 0

to reproduce our results. The 5 corresponds to the number of preds. The 0 is for the edit distance leeway we allow for.

Example of the input is:

torpedo torpille torpille torpilles anti-torpille grenadeur anti-sous-marines
chat bavardage tchat tchatter tchate tchats chatroom
chat chat tchat tchatter tchate tchats chatroom
