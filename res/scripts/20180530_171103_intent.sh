echo firewall
vim-emu compute start -d vnfs_dc -n firewall -i rjpfitscher/genic-vnf --net "(id=input,ip=10.0.0.30/24),(id=output,ip=10.0.0.31/24)" -c ./start_firewall.sh 100 100 100 100 "128KB" 0 &
echo dpi
vim-emu compute start -d vnfs_dc -n dpi -i rjpfitscher/genic-vnf --net "(id=input,ip=10.0.0.40/24),(id=output,ip=10.0.0.41/24)" -c ./start_snort.sh 100 100 100 100 "128KB" 0 &
echo client-firewall
vim-emu network add -b -src client:eth0 -dst firewall:input
echo firewall-dpi
vim-emu network add -b -src firewall:output -dst dpi:input
echo dpi-server
vim-emu network add -b -src dpi:output -dst server:eth0
