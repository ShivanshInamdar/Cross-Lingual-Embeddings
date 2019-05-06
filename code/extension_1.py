import pymagnitude as py
import numpy as np
import sys

def sewing_space_fr_en(eng_mag, fr_mag, b_dict, t_dict, output_f, alpha=0.1):
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
  
  #print('i get here')
  
  en_d = {}
  fr_d = {}
  
  for key in data_dict_fr_to_en.keys():
    en_d[data_dict_fr_to_en[key]] = eng_vectors.query(data_dict_fr_to_en[key])
    fr_d[key] = fr_vectors.query(key)
  
  for key in data_dict_fr_to_en.keys():
    en = en_d[data_dict_fr_to_en[key]] #vector of english word
    fr = fr_d[key] #vector of french word
      
    diff_vec_fr = en - fr
    diff_vec_en = fr - en
      
    en = en + diff_vec_en * alpha
    fr = fr + diff_vec_fr * alpha
    
    en_d[data_dict_fr_to_en[key]] = en
    fr_d[key] = fr
    
  en_mat = []
  fr_mat = []
  for key in data_dict_fr_to_en.keys():
    en = en_d[data_dict_fr_to_en[key]] 
    fr = fr_d[key]
    
    en_mat.append(en)
    fr_mat.append(fr)
  
  
  en_mat = np.array(en_mat)
  fr_mat = np.array(fr_mat)
  
      
  u, sig, vt = np.linalg.svd(np.matmul(en_mat.transpose(), fr_mat))

  W = np.matmul(np.transpose(vt), np.transpose(u))       
      
  final_transform = W#np.matmul(W, WW)    
      
  
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

def sewing_space_en_fr(eng_mag, fr_mag, b_dict, t_dict, output_f, alpha=0.1):
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
  
  #print('i get here')
  
  en_d = {}
  fr_d = {}
  
  for key in data_dict_fr_to_en.keys():
    en_d[data_dict_fr_to_en[key]] = eng_vectors.query(data_dict_fr_to_en[key])
    fr_d[key] = fr_vectors.query(key)
  
  for key in data_dict_fr_to_en.keys():
    en = en_d[data_dict_fr_to_en[key]] #vector of english word
    fr = fr_d[key] #vector of french word
      
    diff_vec_fr = en - fr
    diff_vec_en = fr - en
      
    en = en + diff_vec_en * alpha
    fr = fr + diff_vec_fr * alpha
    
    en_d[data_dict_fr_to_en[key]] = en
    fr_d[key] = fr
    
  en_mat = []
  fr_mat = []
  for key in data_dict_fr_to_en.keys():
    en = en_d[data_dict_fr_to_en[key]] 
    fr = fr_d[key]
    
    en_mat.append(en)
    fr_mat.append(fr)
  
  
  en_mat = np.array(en_mat)
  fr_mat = np.array(fr_mat)
  
      
  u, sig, vt = np.linalg.svd(np.matmul(fr_mat.transpose(), en_mat))

  W = np.matmul(np.transpose(vt), np.transpose(u))       
      
  final_transform = W#np.matmul(W, WW)    
      
  
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
  alpha = float(sys.argv[6])
  direction = sys.argv[7]
  print(alpha)
  if direction == "en-fr":
    sewing_space_en_fr(en_mag, fr_mag, b_dict, t_dict, output_f, alpha)
  elif direction == "fr-en":
    sewing_space_fr_en(en_mag, fr_mag, b_dict, t_dict, output_f, alpha)