from estimate import estimate
from collections import defaultdict

EPSILON = '*e*'

if __name__ == '__main__':
    ep_jp_prob = estimate()
    with open('epron-jpron.wfst', 'w') as fp:
        fp.write('F\n')
        for ep in ep_jp_prob:
            jp_path_prob = defaultdict(float)
            for jp in ep_jp_prob[ep]:
                jp_chars = jp.split()
                path = 'F'
                jp_path_prob[path] = 1.0
                for jpc in jp_chars:
                    path += '_' + jpc
                    jp_path_prob[path] += ep_jp_prob[ep][jp]                    
                    
            
            # print jp_path_prob
            # raw_input()
            for path in jp_path_prob:
                if path == 'F':
                    continue
                next_state = path
                trans = path.split('_')[-1]
                cur_state = path[:-len(trans)-1]                
                # print cur_state, next_state, jp_path_prob[cur_state], jp_path_prob[next_state]
                prob_next_state = jp_path_prob[next_state]/jp_path_prob[cur_state]
                prob_return = (jp_path_prob[cur_state]-jp_path_prob[next_state])/jp_path_prob[cur_state]
                if cur_state == 'F':
                    fp.write('(F (' + ep+next_state +' {:s}'.format(ep)+' '+
                        '{:s}'.format(trans)+' '+'{:.4f}'.format(prob_next_state)+'))\n')
                else:
                    fp.write('('+ep+cur_state+' (' + ep+next_state +' {:s}'.format(EPSILON)+' '+
                        '{:s}'.format(trans)+' '+'{:.4f}'.format(prob_next_state)+'))\n')
                    fp.write('('+ep+cur_state+' (F {:s}'.format(EPSILON)+' '+
                        '{:s}'.format(EPSILON)+' '+'{:.4f}'.format(prob_return)+'))\n')
                    
                
                # fp.write('(F (F '+'{:s}'.format(ep)+' '+'"{:s}"'.format(jp)+' '+'{:.4f}'.format(ep_jp_prob[ep][jp])+'))\n')