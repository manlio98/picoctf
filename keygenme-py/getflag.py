import hashlib

username_trial = b"FREEMAN"

dynamic_flag = []

dynamic_flag.append(hashlib.sha256(username_trial).hexdigest()[4])
dynamic_flag.append(hashlib.sha256(username_trial).hexdigest()[5])        
dynamic_flag.append(hashlib.sha256(username_trial).hexdigest()[3])    
dynamic_flag.append(hashlib.sha256(username_trial).hexdigest()[6])
dynamic_flag.append(hashlib.sha256(username_trial).hexdigest()[2])       
dynamic_flag.append(hashlib.sha256(username_trial).hexdigest()[7])      
dynamic_flag.append(hashlib.sha256(username_trial).hexdigest()[1])       
dynamic_flag.append(hashlib.sha256(username_trial).hexdigest()[8])

print("".join(dynamic_flag))
        