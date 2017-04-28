from estimate import estimate



if __name__ == '__main__':
    ep_jp_prob = estimate()
    with open('epron-jpron.wfst', 'w') as fp:
        fp.write('F\n')
        for ep in ep_jp_prob:
            for jp in ep_jp_prob[ep]:
                fp.write('(F (F '+'{:s}'.format(ep)+' '+'"{:s}"'.format(jp)+' '+'{:.4f}'.format(ep_jp_prob[ep][jp])+'))\n')