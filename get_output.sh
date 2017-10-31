prj_dhs=(Olson_et_al_2014 Firnberg_et_al_2014 Melnikov_et_al_2014)
for prj_dh in ${prj_dhs[@]};
do
echo $prj_dh
cp -fr analysis/$prj_dh/data_comparison/ outputs/$prj_dh/
mkdir outputs/$prj_dh/plots
echo "cp -r analysis/$prj_dh/plots/aas outputs/$prj_dh/plots"
cp -fr analysis/$prj_dh/plots/aas outputs/$prj_dh/plots
done 
