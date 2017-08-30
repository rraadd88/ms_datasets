# `ms_datasets`

Datasets of mutational scanning for testing dms2dfe.

1. Olson_et_al_2014
    Input data: amino acid level mutation counts

2. Firnberg_et_al_2014  
    Input data: codon level mutation counts

3. Melnikov_et_al_2014 
    Input data: fastq
    Note: for analyzing this dataset, first download the input data using `get_seq_data.py` script located in `analysis` folder.
        Usage: `get_seq_data.py Melnikov_et_al_2014`
        fastq files would be downloaded from DDBJ into folder `Melnikov_et_al_2014/data_input`. 

# Downloading datasets

Exaple datasets can be downloaded from the latest release from https://github.com/rraadd88/ms_datasets/releases .
In the folder `ms_dataset`, directory `outputs` contains pre-analysed outputs for validation of run while directory `analysis` can be used to test/analyze different datasets as follows. 

# Run dms2dfe

    cd ms_dataset/analysis
    dms2dfe <project directory>

Here, '<project directory>' can be `Firnberg_et_al_2014`, `Melnikov_et_al_2014` or `Olson_et_al_2014`

# Outputs

The outputs of the run can be vaidated with those kept in 'ms_datasets/outputs'.

# Citations

.. [Melnikov_et_al_2014] Melnikov, A., P. Rogov, L. Wang, A. Gnirke, and T.S. Mikkelsen. 2014. Comprehensive mutational scanning of a kinase in vivo reveals substrate-dependent fitness landscapes. Nucleic Acids Research. 42: 1–8.

.. [Firnberg_et_al_2014] Firnberg, E., J.W. Labonte, J.J. Gray, and M. Ostermeier. 2014. A comprehensive, high-resolution map of a Gene’s fitness landscape. Molecular Biology and Evolution. 31: 1581–1592.

.. [Olson_et_al_2014] Olson, C. Anders, Nicholas C. Wu, and Ren Sun. 2014. “A Comprehensive Biophysical Description of Pairwise Epistasis throughout an Entire Protein Domain.” Current Biology 24 (22): 2643–2651. doi:10.1016/j.cub.2014.09.072. http://dx.doi.org/10.1016/j.cub.2014.09.072.
