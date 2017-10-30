import sys
from os.path import basename,dirname,splitext,exists
from os import makedirs
import pandas as pd
import numpy as np
import subprocess
import logging
logging.basicConfig(format='[%(asctime)s] %(levelname)s\tfrom %(filename)s in %(funcName)s(..): %(message)s',level=logging.DEBUG) 

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def get_seq_data(data_input_dh,data_input_fns):
    if not exists(data_input_dh):
        makedirs(data_input_dh)
    log_fh="%s.get_seq_data.log" % data_input_dh
    log_f = open(log_fh,'a')
    for data_input_fn in data_input_fns:
        data_input_fh="%s/%s" % (data_input_dh,basename(data_input_fn))
        if not exists(data_input_fh):
            if not exists('%s.bz2' % data_input_fh):
                logging.info("downloading: %s [%d/%d]" % (basename(data_input_fh),data_input_fns.index(data_input_fn)+1,len(data_input_fns)))
                com="wget -q ftp://ftp.ddbj.nig.ac.jp/ddbj_database/dra/fastq/SRA082/SRA082074/%s.bz2 --directory-prefix=%s" % (data_input_fn,data_input_dh)
                sub_call_err=subprocess.call(com,shell=True,stdout=log_f, stderr=subprocess.STDOUT)
                subprocess.call("bzip2 %s/%s.bz2" % (data_input_dh,data_input_fn.split('/')[1]) ,shell=True,stdout=log_f, stderr=subprocess.STDOUT)
                if sub_call_err!=0:
                    if not exists('%s.gz' % data_input_fh):                    
                        logging.warning('DDBJ not working, trying ENA')
                        #ENA: eg. ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR129/001/SRR1292901/SRR1292901_1.fastq.gz
                        data_input_fn=data_input_fn.split('/')[1]
                        com="wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/%s/00%s/%s/%s.gz --directory-prefix=%s" % (data_input_fn[:6],data_input_fn[9],data_input_fn[:10],data_input_fn,data_input_dh)
                        logging.info('bash command: $ %s' % com)
                        subprocess.call(com,shell=True,stdout=log_f, stderr=subprocess.STDOUT)
                        sub_call_err=subprocess.call("gunzip %s/%s.gz" % (data_input_dh,data_input_fn) ,shell=True,stdout=log_f, stderr=subprocess.STDOUT)
                        if sub_call_err!=0:
                            logging.warning('ENA too not working')
    log_f.close()
    
# prj_dh=raw_input("Get input data for dataset [project_directory eg. Melnikov_et_al_2014]:")
prj_dh=sys.argv[1]
if exists(prj_dh):
    if 'Melnikov_et_al_2014' in prj_dh:
        data_input_dh="%s/data_input" % prj_dh
        data_input_fns=[    "SRX547509/SRR1292901_1.fastq","SRX547509/SRR1292901_2.fastq",
                            "SRX547496/SRR1292881_1.fastq","SRX547496/SRR1292881_2.fastq",
                            "SRX547413/SRR1292709_1.fastq","SRX547413/SRR1292709_2.fastq",
                            "SRX547764/SRR1293147_1.fastq","SRX547764/SRR1293147_2.fastq", 
                            "SRX547516/SRR1292902_1.fastq","SRX547516/SRR1292902_2.fastq",
                            "SRX547520/SRR1292907_1.fastq","SRX547520/SRR1292907_2.fastq",
                            "SRX547765/SRR1293148_1.fastq","SRX547765/SRR1293148_2.fastq", 
                            "SRX547767/SRR1293150_1.fastq","SRX547767/SRR1293150_2.fastq", ]
        get_seq_data(data_input_dh,data_input_fns)
    else:
        logging.error('seq data not available for : %s' % prj_dh)
else:
    logging.error('do not exist : %s' % prj_dh)
