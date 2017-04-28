from __future__ import division
from collections import defaultdict

def build_epron_jpron_data():
    pron_maping = defaultdict(lambda: defaultdict(int))
    with open('epron-jpron.data', 'r') as fp:        
        epron, jpron, relat = [], [], []
        li = 0
        for line in fp:
            if li%3 == 0:
                epron = line.strip().split()
            elif li%3 == 1:
                jpron = line.strip().split()
            elif li%3 == 2:
                relat = map(int, line.strip().split())
            
            li += 1            
            if li%3 == 0:                
                jpr = ''
                for jn,jp in enumerate(jpron):
                    jpr += jp + ' '                    
                    if jn < len(relat)-1 and relat[jn+1] == relat[jn]:
                        continue
                    jpr = jpr.strip()
                    k = relat[jn] - 1                        
                    pron_maping[epron[k]][jpr] += 1
                    jpr = ''
                
    return pron_maping

def estimate():
    d_ep_jp = build_epron_jpron_data()
    d_ep_jp_prob = defaultdict(lambda: defaultdict(float))

    for ep in d_ep_jp:
        tot = sum([d_ep_jp[ep][jp] for jp in d_ep_jp[ep]])

        for jp in d_ep_jp[ep]:
            if d_ep_jp[ep][jp]/tot > 0.001 and len(jp.split()) < 3:
                d_ep_jp_prob[ep][jp] = d_ep_jp[ep][jp]/tot
    return d_ep_jp_prob



if __name__ == '__main__':
    d_ep_jp_prob = estimate()
    all_eps = d_ep_jp_prob.keys()
    all_eps.sort()
    with open('epron-jpron.probs', 'w') as fp:
        for ep in all_eps:
            for jp in d_ep_jp_prob[ep]:
                fp.write(ep + ' : ' + jp + ' # ' + "{:.4f}".format(d_ep_jp_prob[ep][jp]) + '\n')

