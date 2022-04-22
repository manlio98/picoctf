flag_little_indian = "ocip{FTC0l_I4_t5m_ll0m_y_y3nc42a6a41ÿ}"
flag_big_indian = " "
n = 4
chunks = [flag_little_indian[i:i+n] for i in range(0, len(flag_little_indian), n)]
for i in range(len(chunks)):
    if (len(chunks[i]) == 4):
        flag_big_indian += ''.join(reversed(chunks[i]))
        


print(flag_big_indian+"}")
        


    


   
   