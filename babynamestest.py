import re

def extract_names(filename):

    data = open(filename, "r")
    txt = data.read()

    # Getting the Year
    final_result = []
    y = re.search(r'\d\d\d\d</h3>', txt).group()
    z = re.search(r'Popularity\s*in\s*\d\d\d\d', txt).group()

    y1 = y[:4]
    z1 = z[-4:]

    final_result.append(y1)
    print final_result



    m = re.findall(r'<td>[\w*<>/]+',txt)
    raw_lst = []
    for i in m:
      n = re.findall(r'<td>\w+</td>', i)
      raw_lst.append(n)
      

    def conv_lst(inp_lst):
       lst = []
       for i in inp_lst:
          x = i[4:]
          x1 = x[:-5]
          lst.append(x1)
       return lst
       
    all_lsts = []   
    for j in raw_lst:
       all_lsts.append(conv_lst(j))
       
    frmt_all_lsts = []
    for i in all_lsts:
       req_str = i[1] + " " + i[0]
       frmt_all_lsts.append(req_str)

    frmt_all_lsts.sort()
       

    #print all_lsts

    male_rank = {}
    female_rank = {}
    for k in all_lsts:
        male_rank[k[0]]=k[1]
        female_rank[k[0]] = k[2]
        
    final_result = final_result + frmt_all_lsts
    return final_result
    
    
name_of_file = raw_input("Enter the file name from which you want to extract the data: ")
print extract_names(name_of_file)