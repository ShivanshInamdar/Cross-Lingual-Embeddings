import pymagnitude as py
import numpy as np
import sys

def extension3_fr_eng(eng_mag, fr_mag, b_dict, t_dict, output_f):
  eng_vectors = py.Magnitude(eng_mag)
  fr_vectors = py.Magnitude(fr_mag)

  data_dict_en_to_fr = {}
  data_dict_fr_to_en = {}
  with open(b_dict) as f:
      for line in f:
          pair = line.split(" ")
          pair[1] = pair[1][:-1]
          data_dict_en_to_fr[pair[0]] = pair[0]
          data_dict_fr_to_en[pair[1]] = pair[1]
         
  en_mat = []
  fr_mat = []
  for key in data_dict_fr_to_en.keys():
      en = eng_vectors.query(data_dict_fr_to_en[key]) #vector of english word
      fr = fr_vectors.query(key) #vector of french word
      en_mat.append(en)
      fr_mat.append(fr)
      
  en_mat = np.array(en_mat)
  fr_mat = np.array(fr_mat)
  
  u, sig, vt = np.linalg.svd(np.matmul(en_mat.transpose(), fr_mat))

  W = np.matmul(np.transpose(vt), np.transpose(u))    
      
      
  mapped = np.matmul(en_mat, W)
  
  
  mat_avg = []
  for key in data_dict_fr_to_en.keys():
      en = eng_vectors.query(data_dict_fr_to_en[key]) #vector of english word
      fr = fr_vectors.query(key) #vector of french word
      
      average = (np.matmul(en, W) + fr) / 2
      mat_avg.append(average)

      
  mat_avg = np.array(mat_avg)
   
  uu, sigsig, vtvt = np.linalg.svd(np.matmul(mat_avg.transpose(), mapped))

  WW = np.matmul(np.transpose(vtvt), np.transpose(uu))       
    
      
  final_transform = np.matmul(W, WW)    
  
  final = []
  with open(t_dict) as f:
      for i, line in enumerate(f):
          print(i)
          line = line[:-1]
          pair = line.split(" ")
          line = pair[1] + " " + pair[0]
          topn = eng_vectors.most_similar(np.matmul(fr_vectors.query(pair[1]), final_transform), topn=5)
          for j in range(5):
            word = topn[j][0]
            line = line + " " + word
          final.append(line)
          

  np.savetxt(output_f, final, fmt="%s")

def extension3_eng_fr(eng_mag, fr_mag, b_dict, t_dict, output_f):
  eng_vectors = py.Magnitude(eng_mag)
  fr_vectors = py.Magnitude(fr_mag)

  data_dict_en_to_fr = {}
  data_dict_fr_to_en = {}
  with open(b_dict) as f:
      for line in f:
          pair = line.split(" ")
          pair[1] = pair[1][:-1]
          data_dict_en_to_fr[pair[0]] = pair[0]
          data_dict_fr_to_en[pair[1]] = pair[1]
         
  en_mat = []
  fr_mat = []
  for key in data_dict_fr_to_en.keys():
      en = eng_vectors.query(data_dict_fr_to_en[key]) #vector of english word
      fr = fr_vectors.query(key) #vector of french word
      en_mat.append(en)
      fr_mat.append(fr)
      
  en_mat = np.array(en_mat)
  fr_mat = np.array(fr_mat)
  
  u, sig, vt = np.linalg.svd(np.matmul(fr_mat.transpose(), en_mat))

  W = np.matmul(np.transpose(vt), np.transpose(u))    
      
      
  mapped = np.matmul(en_mat, W)
  
  
  mat_avg = []
  for key in data_dict_fr_to_en.keys():
      en = eng_vectors.query(data_dict_fr_to_en[key]) #vector of english word
      fr = fr_vectors.query(key) #vector of french word
      
      average = (np.matmul(en, W) + fr) / 2
      mat_avg.append(average)

      
  mat_avg = np.array(mat_avg)
   
  uu, sigsig, vtvt = np.linalg.svd(np.matmul(mat_avg.transpose(), mapped))

  WW = np.matmul(np.transpose(vtvt), np.transpose(uu))       
    
      
  final_transform = np.matmul(W, WW)    
  
  final = []
  with open(t_dict) as f:
      for i, line in enumerate(f):
          print(i)
          line = line[:-1]
          pair = line.split(" ")
          line = pair[0] + " " + pair[1]
          topn = fr_vectors.most_similar(np.matmul(eng_vectors.query(pair[0]), final_transform), topn=5)
          for j in range(5):
            word = topn[j][0]
            line = line + " " + word
          final.append(line)
          

  np.savetxt(output_f, final, fmt="%s")

if __name__ == '__main__':
    
  en_mag = sys.argv[1]
  fr_mag = sys.argv[2]
  b_dict = sys.argv[3]
  t_dict = sys.argv[4]
  output_f = sys.argv[5]
  if sys.argv[6] == "en-fr":
    extension3_eng_fr(en_mag, fr_mag, b_dict, t_dict, output_f)
  else:
    extension3_fr_eng(en_mag, fr_mag, b_dict, t_dict, output_f)