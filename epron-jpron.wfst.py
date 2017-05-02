from estimate import estimate

EPSILON = '*e*'

if __name__ == '__main__':
    ep_jp_prob = estimate()
    with open('epron-jpron.wfst', 'w') as fp:
        fp.write('F\n')
        for ep in ep_jp_prob:
            for jp in ep_jp_prob[ep]:
                jp_sounds = jp.split()
                for i,jpc in enumerate(jp_sounds):
                    start = end = transition = ''
                    out = jp_sounds[i]
                    if i == 0:
                        start = 'F'
                        transition = ep
                        end = ep+'_'+jp.replace(' ', '#')+'_'+jp_sounds[i]
                    else:
                        start = ep+'_'+jp.replace(' ', '#')+'_'+'_'.join(jp_sounds[:i])
                        transition = EPSILON
                        end = start + '_' + jpc                    
                    fp.write('({0} ({1} {2} {3} {4}))\n'.format(start, end, transition, out, 1.0))
                    if i == len(jp_sounds)-1:
                        fp.write('({1} ({0} {2} {3} {4}))\n'.format('F', end, EPSILON, EPSILON, ep_jp_prob[ep][jp]))                