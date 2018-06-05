gmt gmtset MAP_FRAME_TYPE fancy
gmt gmtset FONT_TITLE 16,37
gmt gmtset MAP_GRID_PEN_PRIMARY 0.25p,100/100/100,4_2:1

set PS=SNM2015_yushuSNM.ps
set BOUNDARY=..\Data\xsp.xyz 
set L=..\Data\九段线.dat
set DATA=水温月变201407.txt
set R=-R70/15.5/138/54.5r
set J=-JM105/35/7.72i
set BLOCK=..\Data\二级块体.xyz


gmt psxy %R% %J% -T -K  > %PS%
gmt pscoast  %R% %J% -Gwhite -S174/216/230 -Ba10g10 -N1 -W1 -A10000 -K -O --FONT_ANNOT_PRIMARY=10p>> %PS%

gmt surface location2.txt %R% -I1 -Graws0.nc
gmt psclip shengjie.xyz %R% %J% -O -K >> %ps%
gmt grdview raws0.nc %R% %J% -CSNM.cpt -Qs -O -K >> %ps%
gmt psclip -C -O -K >> %ps%
gmt psscale -CSNM.cpt -D8.1i/1.7i/3.8i/0.2i -O -K -Ac -E >> %ps%

gmt psxy %BOUNDARY% %R% %J% -W0.8p  -O -K >> %PS%
gmt psxy %L% %R% %J%  -O -K >> %PS%
gmt psxy locationTaizhan.txt %R% %J% -St0.25c -G0/0/0 -O -K >> %ps%
gmt psclip shengjie.xyz %R% %J% -O -K >> %ps%


gmt psclip -C -O -K >> %ps%
REM 南海
gmt gmtset MAP_FRAME_TYPE plain 
gmt gmtset MAP_FRAME_PEN 0.5p
set R1=-R106/121/3/24
gmt psbasemap %R1% -JM1.12i -B50  -X6.59i -O  -K >> %PS%
gmt pscoast  %R1%  -N1  -W1 -JM  -B0 -Gwhite -S174/216/230 -O -K >>%PS%
gmt psxy  %BOUNDARY% %R1% -JM -W0.5p  -O -K >>%PS%
echo 107 4.3 SouthChinaSea|gmt  pstext %R1% -JM -F+f9,37+a0+jLM -Gwhite -O -K >> %PS%
gmt psxy %L% %R1% -JM -W1p -O -K >> %PS%
gmt psscale -D6.5i/2i/7.5c/0.75c -CSNM.cpt -O -K >> %ps%
gmt psxy  %R% %J% -T -O >> %PS%
gmt ps2raster %ps%
pause