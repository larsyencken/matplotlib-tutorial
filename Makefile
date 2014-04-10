#
#  Makefile
#

.DELETE_ON_ERROR:

default: \
	figures/bubble.png \
	figures/cmap_basic.png \
	figures/cmap_cax.png \
	figures/cmap_clip.png \
	figures/cmap_colorbar.png \
	figures/cmap_colorbaropts.png \
	figures/cmap_custom.png \
	figures/cmap_discrete.png \
	figures/colorpoint.png \
	figures/figure.png \
	figures/formatters.png \
	figures/fourplot_hist.png \
	figures/funcformdate.png \
	figures/latex.png \
	figures/linestyle.png \
	figures/locators.png \
	figures/map.png \
	figures/mappoint.png \
	figures/mapraster.png \
	figures/mapshape.png \
	figures/markersize.png \
	figures/markerstyle.png \
	figures/plot.png \
	figures/point.png \
	figures/pointalpha.png \
	figures/spines.png \
	figures/subplot.png \
	figures/textnomticker.png \
	figures/textproperties.png \
	figures/xyz.png \

clean:
	rm -f figures/*

figures/bubble.png: code/bubble.py
	python code/bubble.py

figures/cmap_basic.png: code/cmap_basic.py
	python code/cmap_basic.py

figures/cmap_cax.png: code/cmap_cax.py
	python code/cmap_cax.py

figures/cmap_clip.png: code/cmap_clip.py
	python code/cmap_clip.py

figures/cmap_colorbar.png: code/cmap_colorbar.py
	python code/cmap_colorbar.py

figures/cmap_colorbaropts.png: code/cmap_colorbaropts.py
	python code/cmap_colorbaropts.py

figures/cmap_custom.png: code/cmap_custom.py
	python code/cmap_custom.py

figures/cmap_discrete.png: code/cmap_discrete.py
	python code/cmap_discrete.py

figures/colorpoint.png: code/colorpoint.py
	python code/colorpoint.py

figures/figure.png: code/figure.py
	python code/figure.py

figures/formatters.png: code/formatters.py
	python code/formatters.py

figures/fourplot_hist.png: code/fourplot.py
	python code/fourplot.py

figures/funcformdate.png: code/funcformdate.py
	python code/funcformdate.py

figures/latex.png: code/latex.py
	python code/latex.py

figures/linestyle.png: code/linestyle.py
	python code/linestyle.py

figures/locators.png: code/locators.py
	python code/locators.py

figures/map.png: code/map.py
	python code/map.py

figures/mappoint.png: code/mappoint.py
	python code/mappoint.py

figures/mapraster.png: code/mapraster.py
	python code/mapraster.py

figures/mapshape.png: code/mapshape.py
	python code/mapshape.py

figures/markersize.png: code/markersize.py
	python code/markersize.py

figures/markerstyle.png: code/markerstyle.py
	python code/markerstyle.py

figures/plot.png: code/plot.py
	python code/plot.py

figures/point.png: code/point.py
	python code/point.py

figures/pointalpha.png: code/pointalpha.py
	python code/pointalpha.py

figures/spines.png: code/spines.py
	python code/spines.py

figures/subplot.png: code/subplot.py
	python code/subplot.py

figures/textnomticker.png: code/textnomticker.py
	python code/textnomticker.py

figures/textproperties.png: code/textproperties.py
	python code/textproperties.py

figures/xyz.png: code/xyz.py
	python code/xyz.py
