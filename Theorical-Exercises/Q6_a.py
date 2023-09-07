import random
N_trials = 10000

def simulate_attack(k, beta, lam):
    success = 0
    for _ in range(N_trials):
        honest_chain = 0 
        private_chain = 0
        while private_chain < k:
            if random.random() < beta/lam: 
                private_chain += 1
            else:    
                honest_chain += 1
        if private_chain >= honest_chain:
            success += 1
    return success/N_trials

ks = [0.1, 0.5, 1, 2]
for lam in ks:
   print(f'λ={lam}: {simulate_attack(6, 0.1, lam)}')
   