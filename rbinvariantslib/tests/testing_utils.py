import os
import requests


def get_file(fname):
    # Download file if not in this directory
    url = f'https://danieldasilva.org/ci_files/rbinvariantslib/{fname}'
    
    if not os.path.exists(fname):
        resp = requests.get(url)
        with open(fname, 'wb') as fh:
            fh.write(resp.content)

    return fname

def get_swmf_file():
    return get_file("./3d__var_1_e20151221-001700-014.out.cdf")


def get_lfm_file():
    return get_file('ElkStorm-LR_mhd_2013-10-04T00-00-00Z.hdf')
